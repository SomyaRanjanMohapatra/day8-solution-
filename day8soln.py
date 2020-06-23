{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "1 2 3 4\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    n = int(raw_input())\n",
    "    arr = map(int, raw_input().split())\n",
    "    m1 = max(arr)\n",
    "    m2 = -9999999999\n",
    "    for i in range(n):\n",
    "        if arr[i] != m1 and arr[i] > m2:\n",
    "            m2 = arr[i]\n",
    "    print m2\n",
    "from collections import Counter\n",
    "if __name__ == '__main__':\n",
    "    n = int(raw_input())\n",
    "    arr = Counter(map(int, raw_input().split())).keys()\n",
    "    arr.sort()\n",
    "    print arr[-2]\n",
    "from collections import Counter\n",
    "if __name__ == '__main__':\n",
    "    n = int(raw_input())\n",
    "    arr = list(set(map(int, raw_input().split())))\n",
    "    arr.sort()\n",
    "    print arr[-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
