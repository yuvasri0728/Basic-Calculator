{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM3/8ziVCf6qsFOsQqrxgQJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yuvasri0728/Basic-Calculator/blob/main/Basic%20Calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XYrGWQ6riF1I",
        "outputId": "a922157a-38d6-4f9a-99cf-74cd23a2a28c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🧮 Basic Arithmetic Operations\n",
            "1. Addition (+)\n",
            "2. Subtraction (-)\n",
            "3. Multiplication (×)\n",
            "4. Division (÷)\n",
            "Choose an operation (1/2/3/4): 2\n",
            "Enter first number: 7\n",
            "Enter second number: 9\n",
            "Result: 7.0 - 9.0 = -2.0\n"
          ]
        }
      ],
      "source": [
        "def add(x, y):\n",
        "    return x + y\n",
        "\n",
        "def subtract(x, y):\n",
        "    return x - y\n",
        "\n",
        "def multiply(x, y):\n",
        "    return x * y\n",
        "\n",
        "def divide(x, y):\n",
        "    if y == 0:\n",
        "        return \"❌ Error: Division by zero!\"\n",
        "    return x / y\n",
        "\n",
        "def main():\n",
        "    print(\"🧮 Basic Arithmetic Operations\")\n",
        "    print(\"1. Addition (+)\")\n",
        "    print(\"2. Subtraction (-)\")\n",
        "    print(\"3. Multiplication (×)\")\n",
        "    print(\"4. Division (÷)\")\n",
        "\n",
        "    choice = input(\"Choose an operation (1/2/3/4): \")\n",
        "\n",
        "    if choice not in ['1', '2', '3', '4']:\n",
        "        print(\"⚠️ Invalid choice.\")\n",
        "        return\n",
        "\n",
        "    try:\n",
        "        num1 = float(input(\"Enter first number: \"))\n",
        "        num2 = float(input(\"Enter second number: \"))\n",
        "    except ValueError:\n",
        "        print(\"⚠️ Invalid input. Please enter numeric values.\")\n",
        "        return\n",
        "\n",
        "    if choice == '1':\n",
        "        print(f\"Result: {num1} + {num2} = {add(num1, num2)}\")\n",
        "    elif choice == '2':\n",
        "        print(f\"Result: {num1} - {num2} = {subtract(num1, num2)}\")\n",
        "    elif choice == '3':\n",
        "        print(f\"Result: {num1} * {num2} = {multiply(num1, num2)}\")\n",
        "    elif choice == '4':\n",
        "        result = divide(num1, num2)\n",
        "        print(f\"Result: {num1} / {num2} = {result}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}