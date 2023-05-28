# Langchain + Linkedin + Twitter

A [Langchain](https://langchain.readthedocs.io/) project that create a summary of a person based on the scraped data from Linkedin and Twitter.

This project is part of the course [Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/).

## Requirements

- Python 3.11
- pip
- pipenv

## Services

- [OpenAI API](https://platform.openai.com/docs/introduction)
- [Google Search Results API](https://serpapi.com/)
- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- [Nubela ProxyCurl](https://nubela.co/proxycurl/)

## Configuration

Make sure you have the following environment variables set:

```bash
nano .zshrc

export PATH="/Users/bruno/Library/Python/3.11/bin:$PATH"
alias python=/Users/bruno/Library/Python/3.11/bin

source .zshrc
```

## Installation

```bash
pipenv shell
pipenv install
```
