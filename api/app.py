# Import required FastAPI components for building the API
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

# Import Pydantic for data validation and settings management
from pydantic import BaseModel

# Import OpenAI client for interacting with OpenAI's API
from openai import OpenAI
import yfinance as yf
from datetime import datetime
from typing import Optional
import os


# Initialize FastAPI application with a title
app = FastAPI(title="Penny Stock Gainers API")

# Configure CORS (Cross-Origin Resource Sharing) middleware
# This allows the API to be accessed from different domains/origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8001", 
        "http://localhost:8000",
        "https://*.vercel.app",
        "https://*.vercel.app/*",
        "https://vercel.app",
        "https://vercel.app/*",
        "*"  # Allow all origins for development
    ],
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers in requests
)


# Define the data model for penny stock data
class PennyStock(BaseModel):
    symbol: str
    company_name: str
    current_price: float
    previous_close: float
    change: float
    change_percent: float
    volume: int
    market_cap: Optional[float] = None
    sector: Optional[str] = None


# Define the data model for chat requests using Pydantic
# This ensures incoming request data is properly validated
class ChatRequest(BaseModel):
    developer_message: str  # Message from the developer/system
    user_message: str  # Message from the user
    model: Optional[str] = "gpt-4.1-mini"  # Optional model selection
    api_key: str  # OpenAI API key for authentication


# Define the main chat endpoint that handles POST requests
@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        # Initialize OpenAI client with the provided API key
        client = OpenAI(api_key=request.api_key)

        # Create an async generator function for streaming responses
        async def generate():
            # Create a streaming chat completion request
            stream = client.chat.completions.create(
                model=request.model,
                messages=[
                    {"role": "developer", "content": request.developer_message},
                    {"role": "user", "content": request.user_message},
                ],
                stream=True,  # Enable streaming response
            )

            # Yield each chunk of the response as it becomes available
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content

        # Return a streaming response to the client
        return StreamingResponse(generate(), media_type="text/plain")

    except Exception as e:
        # Handle any errors that occur during processing
        raise HTTPException(status_code=500, detail=str(e))


# New endpoint for penny stock gainers
@app.get("/api/penny-stocks/gainers")
async def get_penny_stock_gainers(limit: int = 20):
    """
    Get top gainers among penny stocks (stocks under $5)
    """
    try:
        # List of potential penny stock symbols (focusing on common ones)
        penny_stocks = [
            "SNDL",
            "HEXO",
            "ACB",
            "TLRY",
            "CGC",
            "APHA",
            "CRON",
            "OGI",
            "WEED",
            "HMMJ",
            "MJ",
            "YOLO",
            "POTX",
            "THCX",
            "MJXL",
            "HERB",
            "CANE",
            "GRWG",
            "IIPR",
            "SMG",
            "FUV",
            "WKHS",
            "IDEX",
            "SOLO",
            "RIDE",
            "NKLA",
            "HYLN",
            "XL",
            "SPI",
            "SHIP",
            "ZOM",
            "CTRM",
            "MARK",
            "CIDM",
            "NAKD",
            "TOPS",
            "SHIP",
            "GNUS",
            "JAGX",
            "TNXP",
        ]

        stocks_data = []

        for symbol in penny_stocks[:limit]:
            try:
                # Get stock info using yfinance
                stock = yf.Ticker(symbol)
                info = stock.info

                # Get current price and previous close
                hist = stock.history(period="2d")
                if len(hist) >= 2:
                    current_price = hist["Close"].iloc[-1]
                    previous_close = hist["Close"].iloc[-2]
                    change = current_price - previous_close
                    change_percent = (change / previous_close) * 100

                    # Only include if it's a penny stock (under $5) and has positive gain
                    if current_price <= 5.0 and change_percent > 0:
                        stock_data = PennyStock(
                            symbol=symbol,
                            company_name=info.get("longName", symbol),
                            current_price=round(current_price, 4),
                            previous_close=round(previous_close, 4),
                            change=round(change, 4),
                            change_percent=round(change_percent, 2),
                            volume=int(hist["Volume"].iloc[-1]),
                            market_cap=info.get("marketCap"),
                            sector=info.get("sector"),
                        )
                        stocks_data.append(stock_data)

            except Exception:
                # Skip stocks that can't be fetched
                continue

        # Sort by percentage gain (highest first)
        stocks_data.sort(key=lambda x: x.change_percent, reverse=True)

        return {
            "timestamp": datetime.now().isoformat(),
            "total_stocks": len(stocks_data),
            "stocks": stocks_data[:limit],
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching penny stock data: {str(e)}"
        )


# Alternative endpoint using a different data source
@app.get("/api/penny-stocks/gainers/alternative")
async def get_penny_stock_gainers_alternative(limit: int = 20):
    """
    Alternative method to get penny stock gainers using a different approach
    """
    try:
        # This is a fallback method that could be enhanced with other data sources
        # For now, we'll return a message about the primary endpoint
        return {
            "message": "Please use /api/penny-stocks/gainers for the main functionality",
            "endpoint": "/api/penny-stocks/gainers",
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Define a health check endpoint to verify API status
@app.get("/api/health")
async def health_check():
    return {"status": "ok"}


# Root endpoint for Vercel compatibility
@app.get("/")
async def root():
    return {
        "message": "Penny Stock Gainers API",
        "version": "1.0.0",
        "endpoints": {
            "penny_stocks": "/api/penny-stocks/gainers",
            "health": "/api/health",
            "docs": "/docs"
        }
    }


# Entry point for running the application directly
if __name__ == "__main__":
    import uvicorn

    # Start the server on all network interfaces (0.0.0.0) on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
