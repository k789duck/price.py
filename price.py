{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJKtNt28PHMvPYT4TvQk5q",
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
        "<a href=\"https://colab.research.google.com/github/k789duck/price.py/blob/main/price_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yhRdHu29dkcQ"
      },
      "outputs": [],
      "source": [
        "def shopping(shop_file):\n",
        "    shop_dict = {} # 생성할 사전 객체\n",
        "    with open(f\"./data/{shop_file}\") as f:\n",
        "    \n",
        "      for line in f:\n",
        "        words = line.strip().split()\n",
        "        if len(words) == 2:\n",
        "          menu, price_str = words\n",
        "          price_str = price_str.replace(\"원\", \"\")\n",
        "\n",
        "          if menu != \"#쇼핑몰\":\n",
        "            try:\n",
        "              price = int(price_str)\n",
        "            except ValueError:\n",
        "              print(f'Invalid price:{price_str}')\n",
        "\n",
        "            shop_dict[menu] = price\n",
        "\n",
        "    return shop_dict"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def item_price(shop_file, item):\n",
        "  shopping_list = shopping(shop_file)\n",
        "  shopping_price = shopping_list.get(item)\n",
        "\n",
        "  return shopping_price"
      ],
      "metadata": {
        "id": "rAMVidlqdm7r"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
