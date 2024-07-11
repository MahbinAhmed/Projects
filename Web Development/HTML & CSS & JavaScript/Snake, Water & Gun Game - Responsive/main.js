// VARIABLES
let user_inp;
let round;
let count;
let roundsCompleted;
let userPoint;
let computerPoint;
let start = document.getElementById("action")
let container = document.getElementById("container")
let snake = document.getElementById("snake")
let water = document.getElementById("water")
let gun = document.getElementById("gun")
let userPlayground = document.getElementById("userPlayground")
let computerPlayground = document.getElementById("computerPlayground")
let scoreBoard = document.getElementById("scoreBoard")
let game = document.getElementById("game")
let roundResult = document.getElementById("roundResult")
let roundResultText = document.getElementById("roundResultText")
let next = document.getElementById("next")
let gameResult = document.getElementById("gameResult")
let gameResultText = document.getElementById("gameResultText")
let startNew = document.getElementById("startNew")
let select_btn = document.getElementById("select")
let options = computerPlayground.getElementsByClassName("box");

// Final result presenter of each game
function showGameResult(){
    game.style.display = 'none'
    gameResult.style.display = 'flex'
    let text;
    if(userPoint>computerPoint){
        text = `<h2>Congratulations!</h3><br>
        <h3>You've won the game</h3><br><br>`
    }
    else if(userPoint<computerPoint){
        text = `<h2>Better luck next time!</h2><br>
        <h3>Computer have won the game</h3><br><br>`
    }
    else{
        text = `<h2>The score is level!</h2><br>
        <h3>Game tied<h3><br><br>`
    }

    gameResultText.innerHTML = `${text}
            <p>Total rounds:- 3<br>
            Your score:- ${userPoint}<br>
            Computer's score:- ${computerPoint}</p>`
}

// Starting a new game after completing a game
startNew.addEventListener('click', (e)=>{
    init()
})

// Score board presenter
function showScoreBoard(){
    scoreBoard.style.display = 'flex'
    scoreBoard.innerHTML = `
    <h2>Round-${round}</h2>
    <p>
    Round(s) completed:- ${roundsCompleted}<br><br>
    Your score:- ${userPoint}<br>
    Computer's score:- ${computerPoint}
    </p>`
}

// Result text for every game
function resultText(result){
    if(result=='user'){
        return `Round ${round} completed<br>
        You've won the round!`
    }

    else if(result=='computer'){
        return `Round ${round} completed<br>
        Computer have won the round!`
    }

    else{
        return `Round ${round} completed<br>
        Round Tied!`
    }
}

// Starting of a new round
next.addEventListener('click', (e)=>{
    roundResult.style.display = 'none'
    if(round==3){
        showGameResult()
    }
    main()
    game.scrollIntoView({behavior:'smooth'})
})

// Main logic of the game
function showRoundResult(computerChoice){
    // Removing 'selected' class from the options selected by user and computer
    document.getElementById(user_inp).classList.remove('selected')
    options[computerChoice].classList.remove('selected')

    userPlayground.style.display = 'none'
    computerPlayground.style.display = 'none'
    roundResult.style.display = 'flex'
    switch (computerChoice) {
        case 0: // Snake
            if(user_inp=='snake'){
                roundResultText.innerHTML = resultText('tie')
            }
            else if(user_inp=='water'){
                computerPoint += 1;
                roundResultText.innerHTML = resultText('computer')
            }
            else{
                userPoint += 1;
                roundResultText.innerHTML = resultText('user')
            }
            break;
            
            case 1: // Water
            if(user_inp=='snake'){
                userPoint += 1;
                roundResultText.innerHTML = resultText('user')
            }
            else if(user_inp=='water'){
                roundResultText.innerHTML = resultText('tie')
            }
            else{
                computerPoint += 1;
                roundResultText.innerHTML = resultText('computer')
            }
            break;
            
            case 2: // Gun
            if(user_inp=='snake'){
                computerPoint += 1;
                roundResultText.innerHTML = resultText('computer')
            }
            else if(user_inp=='water'){
                userPoint += 1;
                roundResultText.innerHTML = resultText('user')
            }
            else{
                roundResultText.innerHTML = resultText('tie')
            }
            break;
            
            default:
                console.log("Unknown Error Occured!");
                break;
            }
        roundResult.scrollIntoView({behavior:'smooth'})
            if(round==3){
                next.innerHTML = 'Result'
            }
}


// Simple animation during option selection by computer
function computerChoiceAnimation(index, choice){
    count += 1;
    if(count>(6+choice+1)){
        options[choice].classList.add('selected')
        setTimeout(() => {
            showRoundResult(choice)
            roundsCompleted += 1;
            showScoreBoard()
        }, 500);
        return 
    }
    
    options[index].classList.toggle('choosing')
    setTimeout(() => {
        options[index].classList.toggle('choosing')
        if(index<options.length-1){
            computerChoiceAnimation(index+1, choice)
        }
        else{
            computerChoiceAnimation(0, choice)
        }
    }, 550);
}

// Option selector for computer
function computerChoice(){
    computerPlayground.style.display = 'flex'
    computerPlayground.scrollIntoView({behavior:'smooth'})
    let compChoice = Math.floor(Math.random()*3)
    count = 0;
    computerChoiceAnimation(0, compChoice)
}

// Logger of user input and visual responder
function select(option) {
    // Logging user input
    user_inp = option;
    
    // Adding 'selected' class in the chosed option by the user
    let options = Array.from(document.querySelectorAll('.box'));
    for(let item of options){
        item.classList.remove('selected')
    }
    document.getElementById(option).classList.add('selected')
    select_btn.style.display = 'block'
}

// User option selection through click
snake.addEventListener('click', (e) => {
    select('snake')
})

snake.addEventListener('keydown', (e) => {
    if(e.key=='Enter'){
        select('snake')
    }
})

water.addEventListener('click', (e) => {
    select('water')
})

// User option selection through 'Enter' button
water.addEventListener('keydown', (e) => {
    if(e.key=='Enter'){
        select('water')
    }
})

gun.addEventListener('click', (e) => {
    select('gun')
})

gun.addEventListener('keydown', (e) => {
    if(e.key=='Enter'){
        select('gun')
    }
})

// Submitting user's selection
select_btn.addEventListener('click', (e)=>{
    if(user_inp!=null){
        computerChoice();
    }
})

// Starting of every round
function main(){
    userPlayground.style.display = 'flex'
    user_inp = null
    select_btn.style.display = 'none'
    round += 1
    showScoreBoard()
}

// Starting of every game
function init(){
    gameResult.style.display = 'none'
    round = 0;
    roundsCompleted = 0;
    userPoint = 0;
    computerPoint = 0;
    next.innerHTML = 'NEXT'
    container.style.display = 'none'
    game.style.display = 'flex'
    main();
}

// Starting of the program through click
start.addEventListener('click', (e)=>{
    init()
})

// Starting of the program through 'Enter' button
start.addEventListener('keydown', (e)=>{
    if(e.key=='Enter'){
        init()
    }
})