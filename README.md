# 🚀 AI Web Generator

An intelligent web development agent that transforms your ideas into fully functional websites. Simply describe what you want or upload an image, and watch as it generates HTML, CSS, and JavaScript code, then automatically deploys it to GitHub Pages.

## 🎥 Demo Video
[Watch the demo](https://drive.google.com/file/d/1s0AVLIJOpeT3q489oovBdxvxozps8J6j/view?usp=sharing) to see the AI Web Generator in action!

## ✨ Features

- 🤖 **AI-Powered Generation**: Uses Google Gemini AI to understand your requirements
- 📱 **Multi-Input Support**: Accept text prompts or image uploads
- 🎨 **Complete Web Stack**: Generates HTML, CSS, and JavaScript
- 🔄 **Auto Deployment**: Automatically creates GitHub repository and deploys to GitHub Pages
- 🖼️ **Image Recognition**: Replicates designs from uploaded images
- 📐 **Responsive Design**: Creates mobile-friendly websites
- ⚡ **Local Development**: Generates files in your local machine first

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or higher
- Git installed on your system
- GitHub account
- Google Cloud account (for Gemini API)

## 📋 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-web-generator.git
cd ai-web-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Required API Keys

#### GitHub Personal Access Token
1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `workflow` (Update GitHub Action workflows)
   - `write:packages` (Upload packages to GitHub Package Registry)
4. Copy the generated token

#### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Select your Google Cloud project or create a new one
4. Copy the generated API key

### 4. Configure API Keys

**Option 1: Direct Code Modification (Recommended)**

Open your main Python file and replace the placeholder values:

```python
# GitHub Configuration (Replace with your actual tokens)
GITHUB_TOKEN = "your_github_personal_access_token_here"
GITHUB_USERNAME = "your_github_username_here"

# Google Gemini AI Configuration  
GEMINI_API_KEY = "your_gemini_api_key_here"
```

**Option 2: Environment Variables (Optional)**

If you prefer using environment variables, create a `.env` file:

```env
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_USERNAME=your_github_username
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Configure Git (if not already done)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 🚀 Usage

### Run the Application

```bash
python main.py
```

The application will guide you through an interactive setup:

1. **Image Input**: Choose whether to provide an image or text description
   ```
   Do you wanna give image input(y/n)?:- y
   Enter the image path: /path/to/your-design.png
   ```

2. **Project Description**: Describe what you want to create
   ```
   🎯 Describe the project you want to create: Create a modern portfolio website with dark theme
   ```

3. **Project Name**: Enter a name or press Enter for auto-generated name
   ```
   📁 Project name (press Enter for auto-generated): my-portfolio
   ```

4. **GitHub Deployment**: Choose whether to deploy to GitHub
   ```
   🚀 Deploy to GitHub? (y/n): y
   📦 Repository name (default: my-portfolio): 
   ```

5. **Results**: View your generated project and live website
   ```
   🎉 SUCCESS!
   📂 Local project: ./generated/my-portfolio
   🌐 Live website: https://yourusername.github.io/my-portfolio
   ```

## 📦 Requirements

### Python Dependencies (`requirements.txt`)

```
annotated-types==0.7.0
anyio==4.9.0
cachetools==5.5.2
certifi==2025.4.26
charset-normalizer==3.4.2
google-auth==2.40.2
google-genai==1.16.1
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
pyasn1==0.6.1
pyasn1_modules==0.4.2
pydantic==2.11.4
pydantic_core==2.33.2
requests==2.32.3
rsa==4.9.1
sniffio==1.3.1
typing-inspection==0.4.1
typing_extensions==4.13.2
urllib3==2.4.0
websockets==15.0.1
```

### System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.8 or higher
- **Memory**: Minimum 4GB RAM
- **Storage**: 1GB free space
- **Internet**: Required for AI API calls and GitHub operations

## 🎯 Examples

### Example 1: Text-Based Generation
```
Do you wanna give image input(y/n)?:- n
🎯 Describe the project you want to create: Create a minimal portfolio website for a UX designer
📁 Project name (press Enter for auto-generated): ux-portfolio
🚀 Deploy to GitHub? (y/n): y
📦 Repository name (default: ux-portfolio): 
```

### Example 2: Image-Based Generation
```
Do you wanna give image input(y/n)?:- y
Enter the image path: ./designs/mockup.png
🎯 Describe the project you want to create: Replicate this restaurant website design
📁 Project name (press Enter for auto-generated): restaurant-site
🚀 Deploy to GitHub? (y/n): y
```

### Example 3: Local Development Only
```
Do you wanna give image input(y/n)?:- n
🎯 Describe the project you want to create: Modern SaaS landing page with pricing section
📁 Project name (press Enter for auto-generated): saas-landing
🚀 Deploy to GitHub? (y/n): n
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   ```bash
   Error: Invalid API key
   ```
   - Verify your API keys in the placeholder sections of your code
   - Check if the keys have proper permissions

2. **GitHub Permission Errors**
   ```bash
   Error: Permission denied
   ```
   - Ensure your GitHub token has the required scopes
   - Verify your GitHub username is correct

3. **Generation Failures**
   ```bash
   Error: Failed to generate code
   ```
   - Check your internet connection
   - Verify the Gemini API quota hasn't been exceeded

### Debug Mode

If you encounter issues, check the console output for detailed error messages and troubleshooting information during the interactive process.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## 🙏 Acknowledgments

- Google Gemini AI for code generation
- GitHub for hosting and deployment
- Unsplash for placeholder images
- The open-source community for inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/anshkarwasra/WebBuilderCLITool/issues) page
2. Create a new issue with detailed information

## 🔮 Roadmap

- [ ] Support for React/Vue.js generation
- [ ] Database integration capabilities
- [ ] Custom domain configuration
- [ ] Team collaboration features
- [ ] Template marketplace
- [ ] Advanced SEO optimization

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ by [Ansh karwasra]
