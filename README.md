
## Discord-AI-Chatbot-that-speaks-like-Batman 

An AI Chatbot that has been trained to respond like Batman by using DialoGPT model , a generative Pre-Trained Transformer. This Chatbot has then been deployed on Discord using Python through Repl.it
## WorkFlow

- Setup your folder into the google drive and mount it.
- Gather data for your desired character , you can use kaggle or any open source website.
- Design an expression using pythex to read the data accordingly
- Convert it into dataframe
- Import required Dependencies
- Manipulate and set the data to our needs (context dataframe)
- Split the dataset into train and test set
- Create Dataset suitable for our model
- Build model
- Train and Evaluate our model
- Push the Model to Hugging Face
- Create and configure a server to host the bot over there
- Use Repl.it to activate our bot
## Tech Stack

**Language Used:** Python

**IDE Used:** Google Colab , Repl.it


## Deployement

**Google colab:**

- Upload the ipynb files on google colab and before running make sure to mount the google drive according to your specifications

**Discord:**

- Make sure you’re logged on to the Discord website.
- Navigate to the application page.
- Click on the “New Application” button.
- Give the application a name and click “Create”.
- Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!"
*Keep the default settings for Public Bot (checked) and Require OAuth2 Code Grant (unchecked).
Your bot has been created. The next step is to copy the token.*

- Go to the "OAuth2" tab. Then select "bot" under the "scopes" section.
- Now choose the permissions you want for the bot.
- Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.

**Repl.it:**

- Use the repl.it file given and run the bot.
 


## Tips

While working on this project I solved a few errors which might be helpful to others.

-  CUDA/GPU out of memory. Run this python code at the start ( Thanks to [@NicholasRenotte](https://www.youtube.com/c/NicholasRenotte)):

            gpus = tf.config.experimental.list_physical_devices('GPU')
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)

- Repl.it file facing restrictions/errors.

        Windows does poses some reestrictions to host the bot . So try Linux to host the bot it works smoothly over there.
## Special thanks to

 - [freeCodeCamp.org](https://www.youtube.com/c/Freecodecamp)
 - [Lynn Zheng](https://www.freecodecamp.org/news/author/lynn/)
 
 


## Authors

- [@tejasrathod](https://www.linkedin.com/in/tejas-rathod-923187189/)



## License

[MIT](https://github.com/TejasARathod/Discord-AI-Chatbot-that-speaks-like-Batman/blob/12f03ada1a123833270fb1f5b1a2aff1c3fad1a5/LICENSE)


## AI Bot Preview

![](https://github.com/TejasARathod/Discord-AI-Chatbot-that-speaks-like-Batman/blob/12f03ada1a123833270fb1f5b1a2aff1c3fad1a5/1.png)

![](https://github.com/TejasARathod/Discord-AI-Chatbot-that-speaks-like-Batman/blob/12f03ada1a123833270fb1f5b1a2aff1c3fad1a5/2.png)

## Follow the below link to try out my own Batman-Bot

[Click Here](https://huggingface.co/TejasARathod/DialoGPT-medium-BatmanBot?text=hi)




