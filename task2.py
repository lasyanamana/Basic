{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e64bf43f-40ff-45e9-a01b-e62c883d9e60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "May I ask you for your name?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes, we are going to play a game. I am thinking of a number between 1 and 200\n",
      "Go ahead. Guess!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too high\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silly Goose! That number isn't in the range!\n",
      "Please enter a number between 1 and 200\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  18\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too high\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  17\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'name' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 50\u001b[0m\n\u001b[0;32m     48\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m playagain\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myes\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mor\u001b[39;00m playagain\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124my\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mor\u001b[39;00m playagain\u001b[38;5;241m==\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mYes\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m     49\u001b[0m     intro()\n\u001b[1;32m---> 50\u001b[0m     pick()\n\u001b[0;32m     51\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDo you want to play again?\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     52\u001b[0m     playagain\u001b[38;5;241m=\u001b[39m\u001b[38;5;28minput\u001b[39m()\n",
      "Cell \u001b[1;32mIn[1], line 42\u001b[0m, in \u001b[0;36mpick\u001b[1;34m()\u001b[0m\n\u001b[0;32m     40\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m guess \u001b[38;5;241m==\u001b[39m number:\n\u001b[0;32m     41\u001b[0m     guessesTaken \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mstr\u001b[39m(guessesTaken)\n\u001b[1;32m---> 42\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mGood job, \u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;241m+\u001b[39m name \u001b[38;5;241m+\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m! You guessed my number in \u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;241m+\u001b[39m guessesTaken \u001b[38;5;241m+\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m guesses!\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m     44\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m guess \u001b[38;5;241m!=\u001b[39m number:\n\u001b[0;32m     45\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mNope. The number I was thinking of was \u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;241m+\u001b[39m \u001b[38;5;28mstr\u001b[39m(number))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'name' is not defined"
     ]
    }
   ],
   "source": [
    "import random #bring in the random number\n",
    "import time\n",
    "number=random.randint(1, 200) #pick the number between 1 and 200\n",
    "\n",
    "def intro():\n",
    "    print(\"May I ask you for your name?\")\n",
    "    name=input() #asks for the name\n",
    "    print(name + \", we are going to play a game. I am thinking of a number between 1 and 200\")\n",
    "    time.sleep(.5)\n",
    "    print(\"Go ahead. Guess!\")\n",
    "\n",
    "def pick():\n",
    "    guessesTaken = 0\n",
    "    while guessesTaken < 6: #if the number of guesses is less than 6\n",
    "        time.sleep(.25)\n",
    "        enter=input(\"Guess: \") #inserts the place to enter guess\n",
    "        try: #check if a number was entered\n",
    "            guess = int(enter) #stores the guess as an integer instead of a string    \n",
    "\n",
    "            if guess<=200 and guess>=1: #if they are in range\n",
    "                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong\n",
    "                if guessesTaken<6:\n",
    "                    if guess<number:\n",
    "                        print(\"The guess of the number that you have entered is too low\")\n",
    "                    if guess>number:\n",
    "                        print(\"The guess of the number that you have entered is too high\")\n",
    "                    if guess != number:\n",
    "                        time.sleep(.5)\n",
    "                        print(\"Try Again!\")\n",
    "                if guess==number:\n",
    "                    break #if the guess is right, then we are going to jump out of the while block\n",
    "            if guess>200 or guess<1: #if they aren't in the range\n",
    "                print(\"Silly Goose! That number isn't in the range!\")\n",
    "                time.sleep(.25)\n",
    "                print(\"Please enter a number between 1 and 200\")\n",
    "\n",
    "        except: #if a number wasn't entered\n",
    "            print(\"I don't think that \"+enter+\" is a number. Sorry\")\n",
    "            \n",
    "    if guess == number:\n",
    "        guessesTaken = str(guessesTaken)\n",
    "        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')\n",
    "\n",
    "    if guess != number:\n",
    "        print('Nope. The number I was thinking of was ' + str(number))\n",
    "\n",
    "playagain=\"yes\"\n",
    "while playagain==\"yes\" or playagain==\"y\" or playagain==\"Yes\":\n",
    "    intro()\n",
    "    pick()\n",
    "    print(\"Do you want to play again?\")\n",
    "    playagain=input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c6987e63-f213-4745-a4eb-18c70493494d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "May I ask you for your name?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes, we are going to play a game. I am thinking of a number between 1 and 200\n",
      "Go ahead. Guess!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silly Goose! That number isn't in the range!\n",
      "Please enter a number between 1 and 200\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too high\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  70\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  84\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nope. The number I was thinking of was 88\n",
      "Do you want to play again?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " n\n"
     ]
    }
   ],
   "source": [
    "import random #bring in the random number\n",
    "import time\n",
    "number=random.randint(1, 200) #pick the number between 1 and 200\n",
    "\n",
    "def intro():\n",
    "    print(\"May I ask you for your name?\")\n",
    "    name=input() #asks for the name\n",
    "    print(name + \", we are going to play a game. I am thinking of a number between 1 and 200\")\n",
    "    time.sleep(.5)\n",
    "    print(\"Go ahead. Guess!\")\n",
    "\n",
    "def pick():\n",
    "    guessesTaken = 0\n",
    "    while guessesTaken < 6: #if the number of guesses is less than 6\n",
    "        time.sleep(.25)\n",
    "        enter=input(\"Guess: \") #inserts the place to enter guess\n",
    "        try: #check if a number was entered\n",
    "            guess = int(enter) #stores the guess as an integer instead of a string    \n",
    "\n",
    "            if guess<=200 and guess>=1: #if they are in range\n",
    "                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong\n",
    "                if guessesTaken<6:\n",
    "                    if guess<number:\n",
    "                        print(\"The guess of the number that you have entered is too low\")\n",
    "                    if guess>number:\n",
    "                        print(\"The guess of the number that you have entered is too high\")\n",
    "                    if guess != number:\n",
    "                        time.sleep(.5)\n",
    "                        print(\"Try Again!\")\n",
    "                if guess==number:\n",
    "                    break #if the guess is right, then we are going to jump out of the while block\n",
    "            if guess>200 or guess<1: #if they aren't in the range\n",
    "                print(\"Silly Goose! That number isn't in the range!\")\n",
    "                time.sleep(.25)\n",
    "                print(\"Please enter a number between 1 and 200\")\n",
    "\n",
    "        except: #if a number wasn't entered\n",
    "            print(\"I don't think that \"+enter+\" is a number. Sorry\")\n",
    "            \n",
    "    if guess == number:\n",
    "        guessesTaken = str(guessesTaken)\n",
    "        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')\n",
    "\n",
    "    if guess != number:\n",
    "        print('Nope. The number I was thinking of was ' + str(number))\n",
    "\n",
    "playagain=\"yes\"\n",
    "while playagain==\"yes\" or playagain==\"y\" or playagain==\"Yes\":\n",
    "    intro()\n",
    "    pick()\n",
    "    print(\"Do you want to play again?\")\n",
    "    playagain=input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0015eb4b-ca40-4acb-a667-4e5b89dc85c5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
