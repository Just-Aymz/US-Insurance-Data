{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMwIOTcJGpDT7oUi7exXU4C",
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
        "<a href=\"https://colab.research.google.com/github/Just-Aymz/US-Insurance-Data/blob/main/Schema_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        },
        "id": "H0b3_FK9zIwY",
        "outputId": "bb405192-a9b9-4ea0-a1e7-58528baaa62a"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-1-9d85bf104b7c>, line 14)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-9d85bf104b7c>\"\u001b[0;36m, line \u001b[0;32m14\u001b[0m\n\u001b[0;31m    Class Region(Enum):\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "from pydantic import BaseModel\n",
        "from enum import Enum\n",
        "from typing import Optional\n",
        "\n",
        "# Enum for categorical features\n",
        "class SmokerStatus(Enum):\n",
        "    yes = \"yes\"\n",
        "    no = \"no\"\n",
        "\n",
        "class Sex(Enum):\n",
        "    male = \"male\"\n",
        "    female = \"female\"\n",
        "\n",
        "class Region(Enum):\n",
        "    south west = \"southwest\"\n",
        "    south east = \"southeast\"\n",
        "    north west = \"northwest\"\n",
        "    north east = \"northeast\"\n",
        "\n",
        "class InputFeatures(BaseModel):\n",
        "    age: float\n",
        "    bmi: float\n",
        "    children: int\n",
        "    sex: Sex\n",
        "    smoker: SmokerStatus\n",
        "    region: Region\n",
        "\n",
        "    class Config:\n",
        "        use_enum_values = True\n"
      ]
    }
  ]
}
