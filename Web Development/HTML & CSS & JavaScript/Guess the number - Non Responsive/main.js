let start = document.getElementById("start")
let total_attempt;
let score;
let user_inp;

// Result hint
function hint(text){
    let hint = document.getElementById("hint")
    hint.style.display = 'none'
    setTimeout(()=>{
        hint.innerHTML = `${text}`
        hint.style.display = "flex";
    },10);
}

// Result shower of every round
function result(isSuccessful, actual_num){
    let result_box = document.getElementById("result")
    let restart = document.getElementById("restart")
    let hint = document.getElementById("hint")
    let text;
    hint.style.display = 'none'
    input.innerHTML = ''
    note.innerHTML = ''
    result_box.style.display = "flex"
    if(isSuccessful){
        text = "Congratulations, You've entered the correct number!"
        result_box.classList.add("success")
        result_box.classList.remove("failed")
    }
    else{
        text = "You are out of attempts!"
        score = 0;
        result_box.classList.add("failed")
        result_box.classList.remove("success")
    }
    result_box.innerHTML = `<h3>${text}</h3>
    <p>-----------------------------------------<br>
    The correct number is <b>${actual_num};</b><br>
    You've took <b>${total_attempt}</b> ${total_attempt > 1 ? "attempts" : "attempt"};<br>
    Your score is <b>${score}</b>;<br>
    -----------------------------------------</p>`
    restart.style.display = "flex"
    restart.addEventListener('click', (e)=>{
        init()
    })
}

// Logic checker part
function func(user_inp, actual_num){
    if(total_attempt==99){
        total_attempt += 1
        result(false, actual_num)
    }
    else{
        if (user_inp < actual_num) {
            total_attempt += 1;
            score = 100 - total_attempt;
            hint("Enter a greater Number!")
        }
        else if (user_inp == actual_num) {
            total_attempt += 1;
            score = 100 - total_attempt;
            result(true,actual_num)
            return
        }
        else {
            total_attempt += 1;
            score = 100 - total_attempt;
            hint("Enter a lesser number!")
        }
        note.innerHTML = `
    <p>Note: Enter a number from 1 to 100.
    You have <b>${100-total_attempt}</b> ${(100-total_attempt) > 1? "attempts":"attempt"} left.</p>`
    }
}

// Input taker and validator
function main() {
    let input = document.getElementById("input")
    let enter = document.getElementById("enter")
    let actual_num = Math.floor(Math.random() * 100) + 1 //Generating random number
    
    enter.addEventListener('click', (e) => {
        user_inp = input.value;
        if(user_inp===''){
            hint("Please enter a number!")
        }
        else{
            func(user_inp, actual_num)
        }
    })
    input.addEventListener('keydown', (e)=>{
        user_inp = input.value;
        if(e.key=='Enter'){
            if(user_inp===''){
                hint("Please enter a number!")
            }
            else{
                func(user_inp, actual_num)
            }
        }
    })
}

// Initialization of every new round
let input = document.getElementsByClassName("input")[0]
function init(){
    let result_box = document.getElementById("result")
    let restart = document.getElementById("restart")
    let note = document.getElementById("note")
    result_box.style.display = 'none'
    restart.style.display = 'none'
    total_attempt = 0;
    score = 100;
    start.style.display = 'none'
    note.innerHTML = `
    <p>Note: Enter a number from 1 to 100.
    You have <b>${100-total_attempt}</b> ${(100-total_attempt) > 1? "attempts":"attempt"} left.</p>`
    input.innerHTML = `
    <input type="number" name="input" id="input" class="inputBox">
    <button class="inputButton" id="enter">ENTER</button>`
    main()
}

// Starting of the program
start.addEventListener('click', (e) => {
    init()
})