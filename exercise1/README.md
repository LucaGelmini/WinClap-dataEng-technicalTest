# Exercise 1
Implement the "annograms" function that uses the WORD.LST file to return
anagrams of the word given in the "word" parameter.
```python
def annograms(word):
    #Write your code here.
    words = [w.rstrip() for w in open('WORD.LST')]
    raise NotImplementedError
    
if __name__ == "__main__":
    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))
```
WORD.LST in this [link](https://drive.google.com/file/d/1Zc9ZiRNVDEJYfHHPm4OW0NXTXl8wEvpd/view?usp=sharing)