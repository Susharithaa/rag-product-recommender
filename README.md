# RAG Product Recommendation System

A simple **Retrieval Augmented Generation (RAG)** demo application that recommends products using **vector similarity search and an LLM**.

This project is designed to be **lightweight and easy to deploy**, making it suitable for small cloud instances such as **AWS t2.micro**.

---

## 🚀 Features

* Product search using **vector similarity**
* **FAISS vector database** for fast retrieval
* **SentenceTransformer embeddings**
* **OpenAI LLM** for generating recommendations
* Simple **FastAPI backend**
* Minimal **HTML frontend**
* Uses **dummy dataset (100 products)**

---

## 🧠 Architecture

User Query
↓
Embedding Model (MiniLM)
↓
FAISS Vector Search
↓
Top-K Similar Products
↓
LLM Recommendation Generation

---

## 📁 Project Structure

rag-recommendation-app

main.py → FastAPI backend and RAG logic
generate_dataset.py → Script to create dummy dataset
products.json → Stored dataset (100 products)
requirements.txt → Python dependencies
templates/index.html → Simple frontend UI

---

## ⚙️ Installation

Install dependencies:

pip install -r requirements.txt

---

## 📦 Generate Dataset

Run once to create dummy product data:

python generate_dataset.py

This creates:

products.json

---

## ▶️ Run the Application

Start the FastAPI server:

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000

---

## 🔍 Example Queries

Try queries like:

best laptop for work
comfortable headphones for music
durable backpack for travel
wireless mouse for office use
stylish watch for daily wear

---

## 📊 Tech Stack

* **FastAPI** – Backend API
* **FAISS** – Vector similarity search
* **Sentence Transformers** – Embedding model
* **OpenAI GPT-4o Mini** – LLM recommendation generation
* **HTML + JavaScript** – Simple frontend

---

## ☁️ Deployment

This application is lightweight and can be deployed on:

* AWS EC2 (t2.micro / t3.micro)
* Docker containers
* Local machine

---

## 🎯 Purpose

This project demonstrates a **basic RAG pipeline** including:

* Embedding generation
* Vector retrieval
* LLM augmented responses

It is useful for **learning RAG architecture** and experimenting with **LLM-powered recommendation systems**.

---
