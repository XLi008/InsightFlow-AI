
var myName = prompt("Name: ");
var myfavorite_game = prompt("Video Game:");


sentence = (myName + " and my favorite game is: " + myfavorite_game);



const length_max = 10;

let length =  sentence.length 

const total_length = length_max - length

console.log(sentence + " You have " +" " +(total_length) + " words left")


if (total_length <= 0) {
  console.log("RAN OUT OF WORDS")
} 


