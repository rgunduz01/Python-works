{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOdvsIZM7I0BJ8NWFuvNfwH",
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
        "<a href=\"https://colab.research.google.com/github/rgunduz01/Python-works/blob/main/python%20works.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CTJHBr3oxPWO",
        "outputId": "6fbbe131-c46f-4b7f-d3cc-88cad2d141d4"
      },
      "source": [
        "result=range(1,11)\n",
        "print(list(result))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C-VXeNgKK_Lv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "069a1f68-ebb7-4df3-daa2-5c317b122f59"
      },
      "source": [
        "print(len(set('listen to the voice of enlisted')))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "13\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KgUOmkWR5kXY",
        "outputId": "5aedf221-5465-4a99-c147-bfb533cb05ed"
      },
      "source": [
        "numbers = {}\n",
        "\n",
        "numbers['x'] = 12\n",
        "numbers['y'] = 4\n",
        "numbers.update({'z': 3})\n",
        "\n",
        "print(numbers['x'] + numbers['y'] + numbers['z']**2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "25\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kb2c8dPP6xGY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2ae5d359-d695-45bc-90d8-8dcd21eaa45c"
      },
      "source": [
        "words=[\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"]\n",
        "b = [x for x in words if \"e\" in x]\n",
        "b.sort()\n",
        "c = [x for x in words if \"n\" in x]\n",
        "c.sort()\n",
        "d = [x for x in words if \"b\" in x]\n",
        "d.sort()\n",
        "print(f\"[\\n{b},\\n{c},\\n{d}\\n]\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[\n",
            "['ate', 'eat', 'tea'],\n",
            "['nat', 'tan'],\n",
            "['bat']\n",
            "]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "id": "zAvOvOHfSuU5",
        "outputId": "384c727d-e926-4e60-dad7-14e380cd32c7"
      },
      "source": [
        "if condition1:  \n",
        "    execute body1\n",
        "else : # if condition1 is not ensured execute body2\n",
        "    execute body2"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-3-393737c85df9>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    execute body1\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dMziQMqb61u_",
        "outputId": "c8770077-bc63-4875-e7a5-d251be35663d"
      },
      "source": [
        "numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]\n",
        "numbers_10.insert(1,20)\n",
        "print(numbers_10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3bp8GKW57P-7",
        "outputId": "5da4c58b-cede-4971-c7cb-d8abe4d7a983"
      },
      "source": [
        "fruits_vegetables = [\"fruit\", \"vegetable\", [\"apple\", \"banana\", [\"mango\", \"avocado\"]], [\"spinach\", \"broccoli\"]]\n",
        "print(fruits_vegetables[3][0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "spinach\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Th7Ldcmc3nE",
        "outputId": "6fa43121-3ec1-423d-a06f-447112595cfa"
      },
      "source": [
        "numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]\n",
        "set(numbers)\n",
        "frequent=max(set(numbers),key=numbers.count)\n",
        "print(\"En fazla tekrar eden sayı\", frequent)\n",
        "print(numbers.count(frequent), \"kez tekrar etmiştir\")\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "En fazla tekrar eden sayı 3\n",
            "4 kez tekrar etmiştir\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Ey_dP-odncR",
        "outputId": "e26f115e-026b-4d08-a4b3-35b1e5059d77"
      },
      "source": [
        "#set(\"04/14/2021\")\n",
        "küme={\"04/14/2021\"}\n",
        "küme\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'04/14/2021'}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'04/14/2021'}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MuL4UwBwe8u_",
        "outputId": "c8787395-2ef7-4617-aac2-662c1cf8741e"
      },
      "source": [
        "given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]\n",
        "set(given_list)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{1, 2, 3, 4, 5}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q5iDWdVIfkNx",
        "outputId": "3352d706-4510-4c69-99da-96c5d132b65d"
      },
      "source": [
        "kume1=set(\"wellington\")\n",
        "kume2=set(\"washington\")\n",
        "print(kume1.intersection(kume2))\n",
        "print(kume1.union(kume2))\n",
        "print(kume1.difference(kume2))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'g', 'i', 'w', 't', 'o', 'n'}\n",
            "{'g', 's', 'i', 'e', 'a', 'w', 'l', 'h', 't', 'o', 'n'}\n",
            "{'l', 'e'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NjJGzr1AkvhF"
      },
      "source": [
        "if {}:\n",
        "  print(\"ben\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XXOjtNfn9w5U",
        "outputId": "03a9d72e-557b-415a-af4d-1727dcdad6a5"
      },
      "source": [
        "a=set(\"twelve plus one\")\n",
        "b=set(\"eleven plus two\")\n",
        "a==b"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "upJTrY0M-j07",
        "outputId": "b3502d5c-ed26-4a66-829a-fb739ec95664"
      },
      "source": [
        "condition=input(\"Do you feel good\")\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Do you feel goodYES\n",
            "yes\n",
            "no\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7LFyDkbjAce5",
        "outputId": "04c8238b-fd16-4734-a9f2-606ff94a4604"
      },
      "source": [
        "a = input(\"Please write yes or no : \").lower()\n",
        "if a == \"no\":\n",
        "    a = 0\n",
        "print(bool(a)) \n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Please write yes or no : YES\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q8t6a0lDFAd7",
        "outputId": "d2c350c7-5614-4bfc-94a5-1fef25b1e3e4"
      },
      "source": [
        "print(\"Merhaba, \\n\"\n",
        "      \"Şimdi seninle bir tahmin oyunu oynayacağız. \\n\"\n",
        "      \"İpucu: ..., Avrat, Silah\")\n",
        "gizli_kelime = \"At\"\n",
        "tahmin = \"\"\n",
        "tahmin_sayısı = 0\n",
        "tahmin_sınırı = 3\n",
        "tahmin_bitti = False\n",
        "while tahmin != gizli_kelime and not (tahmin_bitti):\n",
        "    if tahmin_sayısı < tahmin_sınırı:\n",
        "        tahmin = input(\"Tahmin nedir?: \")\n",
        "        tahmin_sayısı += 1\n",
        "    else:\n",
        "        tahmin_bitti = True\n",
        "if tahmin_bitti:\n",
        "    print(\"NE yazık ki bilemedin! :( \")\n",
        "else:\n",
        "    print(\"Aferin, bildin :) \")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Merhaba, \n",
            "Şimdi seninle bir tahmin oyunu oynayacağız. \n",
            "İpucu: ..., Avrat, Silah\n",
            "Tahmin nedir?: vatan\n",
            "Tahmin nedir?: at\n",
            "Tahmin nedir?: at\n",
            "NE yazık ki bilemedin! :( \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CE2YSKrF9wlS"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XNUGTwI0FZvy"
      },
      "source": [
        "number=int(input(\"Sayı giriniz :\"))\n",
        "if number %2 == 0 :\n",
        "  print(number, \"even\")\n",
        "  else:\n",
        "    print(number, \"odd\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "id": "65sqozhvIlT7",
        "outputId": "e1826af4-a662-4837-9ace-1d8804f451e6"
      },
      "source": [
        "number1=int(input(\"Sayı giriniz:\"))\n",
        "number2=int(input(\"Sayı giriniz:\"))\n",
        "if (number1>number2) :\n",
        "  print(\"{} is larger than {}\".format{number1,number2})\n",
        "else:\n",
        "  print(\"{} is larger than {}\".format{number2,number1})"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-9105b1a951cf>\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    print(\"{} is larger than {}\".format{number1,number2})\u001b[0m\n\u001b[0m                                       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sczW5Yg4Xkxv"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}