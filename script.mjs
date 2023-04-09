import {readFile, writeFile} from 'fs/promises'
let file = await readFile(new URL("filesUntil0_20.csv", import.meta.url), "utf-8");

const fileData = file.split(/",\s*|\s*"/);
import { config } from "dotenv";
config();
import { Configuration, OpenAIApi } from "openai";

const openai = new OpenAIApi(
  new Configuration({
    apiKey: process.env.API_KEY,
  })
);
const answer = [];
let counter = 0
for (let i = 1; i < fileData.length; i = i + 2) {
  // if(fileData[i].split('\n').length>=25){
    counter++
    openai
    .createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: `refactor the following code - ${fileData[i]} give only refactored code no explaination`,
        },
      ],
    })
    .then((res) => {
      answer.push(res.data.choices[0].message.content.trim());
      writeFile(
        `refactored${i}.py`,
        `${answer[answer.length - 1]}`,
        (err) => {
          if (err) throw err;
          console.log("Data has been added to the file successfully.");
          console.log(answer)
        }
      )
    })
  // }
  
}
console.log(counter)
