# AI Agent Project

A Python-based AI coding agent that can interact with file systems and execute code using Google's Gemini API. This project was built as a fun learning exercise following the [AI Agent Course on Boot.dev](https://www.boot.dev/courses/build-ai-agent-python).

## 🚀 Features

The AI agent can perform the following operations within a secure sandboxed environment:

- **📁 File Operations**: List directories and read file contents
- **✏️ File Writing**: Create and modify files
- **🐍 Code Execution**: Run Python files with optional arguments
- **🤖 AI Integration**: Uses Google's Gemini 2.0 Flash model for intelligent responses
- **🔒 Security**: All operations are constrained to a working directory for safety

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/max-programming/ai_agent.git
   cd ai_agent
   ```

2. **Install dependencies**:

   Install `uv` by following the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

   ```bash
   uv sync
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🎯 Usage

Run the AI agent with a prompt:

```bash
python main.py "Your prompt here"
```

### Examples

```bash
# Ask the agent to analyze files
python main.py "What files are in the calculator directory?"

# Request code execution
python main.py "Run the calculator with the expression '2 + 3'"

# Ask for file modifications
python main.py "Create a new Python file that prints Hello World"

# Enable verbose output
python main.py "List all files" --verbose
```

## 🏗️ Project Structure

```
ai_agent/
├── main.py              # Main entry point
├── call_function.py     # Function call dispatcher
├── config.py           # Configuration settings
├── functions/          # Available agent functions
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/         # Example calculator app (working directory)
│   ├── main.py
│   ├── pkg/
│   └── README.md
└── tests.py           # Test suite
```

## 🧠 How It Works

1. **User Input**: You provide a natural language prompt
2. **AI Planning**: The Gemini model analyzes your request and creates a function call plan
3. **Function Execution**: The agent executes the appropriate functions (file operations, code execution, etc.)
4. **Iterative Process**: The agent can make multiple function calls to complete complex tasks
5. **Response**: You receive the final result or output

## 🔧 Available Functions

The AI agent has access to these function tools:

- `get_files_info(directory)` - Lists files and directories with metadata
- `get_file_content(file_path)` - Reads file contents (limited to 10,000 characters)
- `write_file(file_path, content)` - Creates or overwrites files
- `run_python_file(file_path, args)` - Executes Python files with arguments

## 🔐 Security Features

- All file operations are restricted to the configured working directory (`./calculator`)
- Path traversal attacks are prevented through absolute path validation
- File execution is limited to Python files only
- Subprocess execution has a 30-second timeout limit

## 📚 Learning Notes

This project demonstrates:

- **Function Calling**: How to integrate AI models with custom functions
- **Security Practices**: Safe file system operations in AI applications
- **API Integration**: Working with Google's Gemini API
- **Error Handling**: Robust exception handling for file operations
- **Modular Design**: Clean separation of concerns with function modules

## 🎓 Course Reference

Built following the excellent [AI Agent Course](https://www.boot.dev/courses/build-ai-agent-python) on Boot.dev. The course covers:

- AI agent architecture
- Function calling with LLMs
- Security considerations
- Real-world implementation patterns

## 📝 License

This is a learning project - feel free to use it for educational purposes!

## 🤝 Contributing

This is primarily a learning project, but feel free to fork it and experiment with your own improvements!

---

_Happy coding! 🚀_
