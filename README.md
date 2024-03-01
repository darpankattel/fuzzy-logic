
# FuzzyLogic Student Learning Level Recommender

## Introduction
Welcome to the FuzzyLogic Student Learning Level Recommender project! This project utilizes fuzzy logic principles to recommend student learning levels across multiple domains, including listening, vocabulary, structure, and reading. Inspired by L. A. Zadeh's pioneering work on fuzzy sets, this system offers educators a powerful tool for personalized assessment and instruction.

## Features
- Provides recommendations for student learning levels based on input marks.

- Utilizes fuzzy logic principles to handle imprecise and uncertain data.

- Offers insights into student proficiency across multiple domains.

## Setup
To set up the project, follow these steps:

+ Clone the repository from GitHub:
```bash
git clone https://github.com/darpankattel/fuzzy-logic.git
```
+ Navigate to the project directory:
```bash
cd fuzzy-logic
```
+ Create a virtual Environment and then activate:
```bash
./env/bin/activate
```
+ Install the required dependencies:
```bash
pip install -r requirements.txt
```
+ Run the project: 
```bash
python main.py
```

## Fuzzy Set Formation
The determination of variables and the formation of
fuzzy sets for each variable used are **Listening,
Vocabulary, Structure, and Reading**. The fuzzy sets
formed from each of these variables are as follows:
1. Listening Variables:
![Listening Fuzzy Set](https://cdn.discordapp.com/attachments/1068715664921088071/1213166738095611944/Screenshot_2024-03-01_223520.png?ex=65f47c91&is=65e20791&hm=e21c1ea4bc3827b73b96d73430e07e77f5fa6220aa3f2404d9559679e5dc5f6c&)
The curve that is formed to determine the
membership function of the foundation variables can
be seen in Figure 1.
![Listening Variable Membership Function](https://cdn.discordapp.com/attachments/1068715664921088071/1213167196856131696/image.png?ex=65f47cff&is=65e207ff&hm=682beea75020b09bd96212175b6d7699b7256c46877da9378559d36d8637e83c&)

2. Vocabulary Variables:
![Vocabulary Fuzzy Set](https://cdn.discordapp.com/attachments/1068715664921088071/1213167683382681611/Screenshot_2024-03-01_223959.png?ex=65f47d73&is=65e20873&hm=3a672ec213b92178d96582cbbf69ef8a540afeda659a9f4989d8201b5447aeee&)
The curve that is formed to determine the
membership function of the vocabulary variable can
be seen in Figure 2.
![Vocabulary Variable Membership Function](https://cdn.discordapp.com/attachments/1068715664921088071/1213167986110631996/Screenshot_2024-03-01_224114.png?ex=65f47dbb&is=65e208bb&hm=fced6afe0532fcf890c52ccf101127f0f316a8ded775180c507c47ea9c253eef&)

3. Structure Variable
![Structure Fuzzy Set](https://cdn.discordapp.com/attachments/1068715664921088071/1213168368442679427/Screenshot_2024-03-01_224246.png?ex=65f47e16&is=65e20916&hm=efcfbf3f5b8e7277ae90976702b216d62e10ce18489d3fbf50610ca8ca269a5a&)
The curve that is formed to determine the
membership function in the structure variable can be
seen in Figure 3.
![Strucutre Variable Membership function](https://cdn.discordapp.com/attachments/1068715664921088071/1213168586080649236/Screenshot_2024-03-01_224339.png?ex=65f47e4a&is=65e2094a&hm=d03ae6827a0ff35133b8b08fe879eb5e80015c23d148946ece04e4073ff4d561&)

4. Reading Variable
![Reading Variable](https://cdn.discordapp.com/attachments/1068715664921088071/1213168869221474335/Screenshot_2024-03-01_224447.png?ex=65f47e8e&is=65e2098e&hm=b2080aba255bdce32bc256f9662c5eac80463b9fce1024aedcb0ad54b5a0dc11&)

The curve that is formed to determine the
membership function in the reading variable can be
seen in Figure 4.

![Reading variable membership function](https://cdn.discordapp.com/attachments/1068715664921088071/1213169101745299577/Screenshot_2024-03-01_224540.png?ex=65f47ec5&is=65e209c5&hm=78ba621be8cf107c312e09193e011227b7b4aa88693d441f7abdfe32aad8a898&)

5. Output Variables
![Fuzzy Set of Output Variables](https://cdn.discordapp.com/attachments/1068715664921088071/1213169383069978746/Screenshot_2024-03-01_224650.png?ex=65f47f08&is=65e20a08&hm=91580a66fe6ecea4a1b57d4445cca05a69ed224379b7b29e06d3e983e3062b16&)
The curve that is formed to determine the
membership function in the output variable can be
seen in Figure 5.

![Output variable membership function](https://cdn.discordapp.com/attachments/1068715664921088071/1213169612993331240/Screenshot_2024-03-01_224739.png?ex=65f47f3f&is=65e20a3f&hm=aee403054c9ffa9b30daba61a86e7719ec605427af1d19a3aef3be2a6511e36b&)


## Membership Functions and Rules
All the Membership functions and Rules are mentioned in the code itself.