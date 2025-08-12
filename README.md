<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>


## <h1 align="center" id="heading"> 👋 Welcome to the AI Engineer Challenge</h1>

## 🤖 Your First Vibe Coding LLM Application

> If you are a novice, and need a bit more help to get your dev environment off the ground, check out this [Setup Guide](docs/GIT_SETUP.md). This guide will walk you through the 'git' setup you need to get started.

> For additional context on LLM development environments and API key setup, you can also check out our [Interactive Dev Environment for LLM Development](https://github.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers).

In this repository, we'll walk you through the steps to create a LLM (Large Language Model) powered application with a vibe-coded frontend!

Are you ready? Let's get started!

<details>
  <summary>🖥️ Accessing "gpt-4.1-mini" (ChatGPT) like a developer</summary>

1. Head to [this notebook](https://colab.research.google.com/drive/1sT7rzY_Lb1_wS0ELI1JJfff0NUEcSD72?usp=sharing) and follow along with the instructions!

2. Complete the notebook and try out your own system/assistant messages!

That's it! Head to the next step and start building your application!

</details>


<details>
  <summary>🏗️ Forking & Cloning This Repository</summary>

Before you begin, make sure you have:

1. 👤 A GitHub account (you'll need to replace `YOUR_GITHUB_USERNAME` with your actual username)
2. 🔧 Git installed on your local machine
3. 💻 A code editor (like Cursor, VS Code, etc.)
4. ⌨️ Terminal access (Mac/Linux) or Command Prompt/PowerShell (Windows)
5. 🔑 A GitHub Personal Access Token (for authentication)

Got everything in place? Let's move on!

1. Fork [this](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge) repo!

     ![image](https://i.imgur.com/bhjySNh.png)

1. Clone your newly created repo.

     ``` bash
     # First, navigate to where you want the project folder to be created
     cd PATH_TO_DESIRED_PARENT_DIRECTORY

     # Then clone (this will create a new folder called The-AI-Engineer-Challenge)
     git clone git@github.com:<YOUR GITHUB USERNAME>/The-AI-Engineer-Challenge.git
     ```

     > Note: This command uses SSH. If you haven't set up SSH with GitHub, the command will fail. In that case, use HTTPS by replacing `git@github.com:` with `https://github.com/` - you'll then be prompted for your GitHub username and personal access token.

2. Verify your git setup:

     ```bash
     # Check that your remote is set up correctly
     git remote -v

     # Check the status of your repository
     git status

     # See which branch you're on
     git branch
     ```

     <!-- > Need more help with git? Check out our [Detailed Git Setup Guide](docs/GIT_SETUP.md) for a comprehensive walkthrough of git configuration and best practices. -->

3. Open the freshly cloned repository inside Cursor!

     ```bash
     cd The-AI-Engineering-Challenge
     cursor .
     ```

4. Check out the existing backend code found in `/api/app.py`

</details>

<details>
  <summary>🔥Setting Up for Vibe Coding Success </summary>

While it is a bit counter-intuitive to set things up before jumping into vibe-coding - it's important to remember that there exists a gradient betweeen AI-Assisted Development and Vibe-Coding. We're only reaching *slightly* into AI-Assisted Development for this challenge, but it's worth it!

1. Check out the rules in `.cursor/rules/` and add theme-ing information like colour schemes in `frontend-rule.mdc`! You can be as expressive as you'd like in these rules!
2. We're going to index some docs to make our application more likely to succeed. To do this - we're going to start with `CTRL+SHIFT+P` (or `CMD+SHIFT+P` on Mac) and we're going to type "custom doc" into the search bar. 

     ![image](https://i.imgur.com/ILx3hZu.png)
3. We're then going to copy and paste `https://nextjs.org/docs` into the prompt.

     ![image](https://i.imgur.com/psBjpQd.png)

4. We're then going to use the default configs to add these docs to our available and indexed documents.

     ![image](https://i.imgur.com/LULLeaF.png)

5. After that - you will do the same with Vercel's documentation. After which you should see:

     ![image](https://i.imgur.com/hjyXhhC.png) 

</details>

<details>
  <summary>😎 Vibe Coding a Front End for the FastAPI Backend</summary>

1. Use `Command-L` or `CTRL-L` to open the Cursor chat console. 

2. Set the chat settings to the following:

     ![image](https://i.imgur.com/LSgRSgF.png)

3. Ask Cursor to create a frontend for your application. Iterate as much as you like!

4. Run the frontend using the instructions Cursor provided. 

> NOTE: If you run into any errors, copy and paste them back into the Cursor chat window - and ask Cursor to fix them!

> NOTE: You have been provided with a backend in the `/api` folder - please ensure your Front End integrates with it!

</details>

<details>
  <summary>🚀 Deploying Your First LLM-powered Application with Vercel</summary>

1. Ensure you have signed into [Vercel](https://vercel.com/) with your GitHub account.

2. Ensure you have `npm` (this may have been installed in the previous vibe-coding step!) - if you need help with that, ask Cursor!

3. Run the command:

     ```bash
     npm install -g vercel
     ```

4. Run the command:

     ```bash
     vercel
     ```

5. Follow the in-terminal instructions. (Below is an example of what you will see!)

     ![image](https://i.imgur.com/D1iKGCq.png)

6. Once the build is completed - head to the provided link and try out your app!

> NOTE: Remember, if you run into any errors - ask Cursor to help you fix them!

</details>

### Vercel Link to Share

You'll want to make sure you share you *domains* hyperlink to ensure people can access your app!

![image](https://i.imgur.com/mpXIgIz.png)

> NOTE: Test this is the public link by trying to open your newly deployed site in an Incognito browser tab!

### 🎉 Congratulations! 

You just deployed your first LLM-powered application! 🚀🚀🚀 Get on linkedin and post your results and experience! Make sure to tag us at @AIMakerspace!

Here's a template to get your post started!

```
🚀🎉 Exciting News! 🎉🚀

🏗️ Today, I'm thrilled to announce that I've successfully built and shipped my first-ever LLM using the powerful combination of , and the OpenAI API! 🖥️

Check it out 👇
[LINK TO APP]

A big shoutout to the @AI Makerspace for all making this possible. Couldn't have done it without the incredible community there. 🤗🙏

Looking forward to building with the community! 🙌✨ Here's to many more creations ahead! 🥂🎉

Who else is diving into the world of AI? Let's connect! 🌐💡

#FirstLLMApp 
```

# Penny Stock Gainers App

A comprehensive web application that displays top gainers in penny stocks in the US market. Built with FastAPI backend and modern HTML/CSS/JavaScript frontend.

## Features

- **Real-time Stock Data**: Fetches live penny stock data using Yahoo Finance API
- **Top Gainers Tracking**: Displays stocks with the highest percentage gains
- **Penny Stock Focus**: Specifically targets stocks under $5.00
- **Beautiful UI**: Modern, responsive design with glassmorphism effects
- **Auto-refresh**: Automatically updates data every 5 minutes
- **Interactive Controls**: Adjustable limits and manual refresh options
- **Market Statistics**: Overview of total stocks, average gains, and top performers
- **Mobile Responsive**: Works seamlessly on all device sizes

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **yfinance**: Yahoo Finance API wrapper for stock data
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running the application

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid, Flexbox, and animations
- **JavaScript ES6+**: Class-based architecture with async/await
- **Font Awesome**: Icons for enhanced UI
- **Google Fonts**: Inter font family for typography

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Backend Setup

1. Navigate to the API directory:
```bash
cd api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
python app.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in your web browser or serve it using a local server:
```bash
# Using Python
python -m http.server 8001

# Using Node.js (if you have it installed)
npx serve .

# Using PHP (if you have it installed)
php -S localhost:8001
```

## API Endpoints

### Penny Stock Gainers
- **GET** `/api/penny-stocks/gainers`
- **Query Parameters**: `limit` (default: 20)
- **Response**: List of penny stocks with highest gains

### Health Check
- **GET** `/api/health`
- **Response**: API status confirmation

### Chat Endpoint (Legacy)
- **POST** `/api/chat`
- **Body**: ChatRequest model with OpenAI integration

## Data Model

### PennyStock
```json
{
  "symbol": "SNDL",
  "company_name": "Sundial Growers Inc.",
  "current_price": 1.2345,
  "previous_close": 1.2000,
  "change": 0.0345,
  "change_percent": 2.88,
  "volume": 1234567,
  "market_cap": 1234567890,
  "sector": "Healthcare"
}
```

## Stock Categories

The app focuses on common penny stock categories:
- **Cannabis/Healthcare**: SNDL, HEXO, ACB, TLRY, CGC
- **Electric Vehicles**: FUV, WKHS, IDEX, SOLO, RIDE, NKLA
- **Technology**: MARK, CIDM, GNUS, TNXP
- **Shipping/Transport**: SHIP, TOP
- **And many more...**

## Configuration

### Backend Configuration
- **Port**: 8000 (configurable in `app.py`)
- **CORS**: Enabled for all origins
- **Data Source**: Yahoo Finance API via yfinance

### Frontend Configuration
- **API URL**: `http://localhost:8000` (configurable in JavaScript)
- **Auto-refresh**: 5 minutes (configurable in JavaScript)
- **Default Limit**: 20 stocks

## Usage

1. **Start the Backend**: Run the FastAPI server
2. **Open Frontend**: Navigate to the frontend HTML file
3. **Fetch Data**: Click "Fetch Stocks" or wait for auto-refresh
4. **Adjust Settings**: Modify the number of stocks to display
5. **Monitor Performance**: View market statistics and individual stock cards

## Features in Detail

### Stock Cards
Each stock is displayed in a beautiful card showing:
- Stock symbol and company name
- Current price and previous close
- Dollar and percentage change
- Trading volume and market cap
- Sector classification

### Market Overview
Real-time statistics including:
- Total number of stocks found
- Average percentage gain
- Top performing stock
- Last update timestamp

### Responsive Design
- **Desktop**: Multi-column grid layout
- **Tablet**: Adaptive grid with optimized spacing
- **Mobile**: Single-column layout with touch-friendly controls

## Error Handling

- **Network Errors**: Graceful fallback with user-friendly messages
- **Data Validation**: Pydantic models ensure data integrity
- **API Failures**: Comprehensive error logging and user feedback
- **Stock Fetching**: Individual stock failures don't break the entire system

## Performance Considerations

- **Async Operations**: Non-blocking API calls for better responsiveness
- **Data Caching**: Efficient data fetching with minimal API calls
- **Optimized Rendering**: Efficient DOM manipulation and updates
- **Memory Management**: Proper cleanup of intervals and event listeners

## Security Features

- **CORS Configuration**: Proper cross-origin resource sharing
- **Input Validation**: Server-side validation of all parameters
- **Error Sanitization**: Safe error messages without sensitive information
- **Rate Limiting**: Built-in protection against excessive requests

## Future Enhancements

- **Real-time WebSocket Updates**: Live price updates
- **Historical Data Charts**: Price movement visualization
- **Portfolio Tracking**: Save and monitor favorite stocks
- **Alert System**: Price change notifications
- **Advanced Filtering**: Sector, market cap, and volume filters
- **Export Functionality**: CSV/PDF export of stock data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the FAQ section
2. Review the API documentation
3. Open an issue on GitHub

## Disclaimer

This application is for informational purposes only. Stock data is provided by Yahoo Finance and may have delays. Always do your own research before making investment decisions. The developers are not responsible for any financial losses.
