
var myName = prompt("Name: ").capitalize();
var myfavorite_game = prompt("Video Game:");


sentence = (myName + " and my favorite game is: " + myfavorite_game).toLowerCase();



const length_max = 10;

let length =  sentence.length 

const total_length = length_max - length

console.log(sentence + " You have " +" " +(total_length) + " words left")


if (total_length <= 0) {
  console.log("RAN OUT OF WORDS");
} 

function array(){
  for (let i = 0; i < 5; i++) {

  var arrays = [2 * 2];
    
  if(arrays.length > 0){
      array = [2 + 3 && 3 ** 2, 4* 2], log(32);
  

  }
 return array;
    }
}


function bmiCalculator (weight, height) {
  var BMI = weight / height ** 2
  BMI = Math.round(BMI)
  if (BMI < 18.5 ){
     var interpretation =  ("Your BMI is, " + BMI + " so you are underweight.");
  }
  else if (BMI >= 18.5 && BMI < 24.5)
  {
     var interpretation =  ("Your BMI is, " + BMI + " so you are normal weight.");
  }
  else if (BMI >= 25 && BMI < 29.9)
  {
     var interpretation =  ("Your BMI is, " + BMI + " so you have are overweight.");
  }
   else if (BMI >= 30 && BMI < 34.4)
  {
     var interpretation =  ("Your BMI is, " + BMI + " so you have are obese.");
  }
   else if (BMI >= 35)
  {
     var interpretation =  ("Your BMI is, " + BMI + " so you have a Extremely obese.");
  }

  return interpretation;
}





console.log(arrays);
