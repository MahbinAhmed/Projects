let radioAny = document.getElementById("any")
let radioCustom = document.getElementById("custom")
let customOptionsDiv = document.getElementsByClassName("customOptionsDiv")[0]
let customPrintButton = document.getElementById("customPrintButton")
let blacklistDiv = document.getElementsByClassName("blacklistDiv")[0]
let blacklistPrintButton = document.getElementById("blacklistPrintButton")
let typeDiv = document.getElementsByClassName("typeDiv")[0]
let typePrintButton = document.getElementById("typePrintButton")
let settingsContainer = document.getElementsByClassName("settingsContainer")[0]
let container1 = document.getElementsByClassName("container1")[0]
let container2 = document.getElementsByClassName("container2")[0]
let category = radioAny.value;
let blacklist = '';
let type = '';
let url;

function urlCleaner(needAnd) {
    let foundQuestionMark = false
    let foundAnd = false
    for (let i = 0; i < url.length; i++) {
        if (url[i] === '?') {
            if (foundQuestionMark === false) {
                foundQuestionMark = true
            }
            else {
                url = url.slice(0, i) + url.slice(i + 1)
                i--;
            }
        }
        else if (url[i] === '&') {
            if (needAnd === false) {
                url = url.slice(0, i) + url.slice(i + 1)
                i--;
            }
            else if (foundAnd === false) {
                foundAnd = true
            }
            else {
                url = url.slice(0, i) + url.slice(i + 1)
                i--;
            }
        }
    }
}

function getUrl() {
    let needAnd = false

    if (blacklist.length > 0) {
        blacklist = '?' + blacklist
        if (type.length > 0) {
            type = '&' + type
            needAnd = true
        }
    }
    else {
        if (type.length > 0) {
            type = '?' + type
        }
    }
    url = 'https://v2.jokeapi.dev/joke/' + category + blacklist + type
    urlCleaner(needAnd)
    console.log(url)
}

let getCategory = () => {
    let customOptionsName = document.querySelectorAll("input[name='customOptionsName']:checked")
    if (customOptionsName.length === 6 || customOptionsName.length === 0) {
        category = radioAny.value
    }
    else {
        category = ''
        for (let i = 0; i < customOptionsName.length; i++) {
            if (i === (customOptionsName.length - 1)) {
                category += customOptionsName[i].value
            }
            else {
                category += customOptionsName[i].value + ','
            }
        }
    }
}

let setLocalStorageCategory = () =>{
    let setCustomSelectionsList = [];
    for(const item of document.querySelectorAll("input[name='customOptionsName']")){
        if(!item.checked){
            setCustomSelectionsList.push(item.id)
        }
    }
    localStorage.setItem("customSelections", JSON.stringify(setCustomSelectionsList))
}

let getBlacklist = () => {
    let blacklistName = document.querySelectorAll("input[name='blacklistName']:checked")
    if (blacklistName.length !== 0) {
        blacklist = 'blacklistFlags='
        for (let i = 0; i < blacklistName.length; i++) {
            if (i === (blacklistName.length - 1)) {
                blacklist += blacklistName[i].value
            }
            else {
                blacklist += blacklistName[i].value + ','
            }
        }
    }
    else {
        blacklist = ''
    }
}

let setLocalStorageBlacklist = () =>{
    let setBlacklistSelectionsList = []
    for(const item of document.querySelectorAll("input[name='blacklistName']:checked")){
        setBlacklistSelectionsList.push(item.id)
    }
    localStorage.setItem("blacklistNotSelections", JSON.stringify(setBlacklistSelectionsList))
}

let getType = () => {
    let typeName = document.querySelectorAll("input[name='typeName']:checked")
    if (typeName.length === 1) {
        type += 'type=' + typeName[0].value
    }
    else {
        type = ''
    }
}

let setLocalStorageType = () =>{
    let setTypeSelectionsList = []
    for(const item of document.querySelectorAll("input[name='typeName']")){
        if(item.checked===false){
            setTypeSelectionsList.push(item.id)
        }
    }
    localStorage.setItem("typeSelections", JSON.stringify(setTypeSelectionsList))
}

const getJoke = async () => {
    getUrl()
    let response = await fetch(url)
    let data = await response.json()
    if (data.type === 'twopart') {
        container1.innerHTML = `<p>*** ${data.setup}</p>`
        container2.innerHTML = `<p>--> ${data.delivery}</p>`
    }
    else {
        container1.innerHTML = `<p>--> ${data.joke}</p>`
    }
}

let radioAnySelect = () => {
    radioAny.checked = true
    category = radioAny.value
    localStorage.setItem("category", "Any")
    customOptionsDiv.style.display = 'none'
}

radioAny.addEventListener('change', ()=>{
    radioAnySelect()
    getUrl()
})

let radioCustomSelect = () => {
    radioCustom.checked = true
    getCategory()
    localStorage.setItem("category", "custom")
    customOptionsDiv.style.display = 'block'
}

radioCustom.addEventListener('change', ()=>{
    radioCustomSelect()
    getUrl()
})

customOptionsDiv.addEventListener('change', () => {
    getCategory()
    setLocalStorageCategory()
    getUrl()
})

blacklistDiv.addEventListener('change', () => {
    getBlacklist()
    setLocalStorageBlacklist()
    getUrl()
})

typeDiv.addEventListener('change', () => {
    getType()
    setLocalStorageType()
    getUrl()
})


function startProgram(){
    let lsCategory = localStorage.getItem("category")
    if(lsCategory==="Any"){
        radioAnySelect()
    }
    else if(lsCategory==="custom"){
        radioCustomSelect()
        let getCustomSelectionsList = JSON.parse(localStorage.getItem("customSelections"))
        for(const item of getCustomSelectionsList){
            document.getElementById(item).checked = false
        }
    }
    else{
        radioAnySelect()
    }
    
    let lsBlacklist = localStorage.getItem("blacklistNotSelections")
    if(lsBlacklist!==null){
        let getBlacklistSelectionList = JSON.parse(localStorage.getItem("blacklistNotSelections"))
        for(const item of getBlacklistSelectionList){
            document.getElementById(item).checked = true
        }
    }
    
    let lsType = localStorage.getItem("typeSelections")
    if(lsType!==null){
        let getTypeSelectionsList = JSON.parse(localStorage.getItem("typeSelections"))
        for(const item of getTypeSelectionsList){
            document.getElementById(item).checked = false
        }
    }
    
    getCategory()
    getBlacklist()
    getType()
    getUrl()
    getJoke()
}

startProgram()

// DESIGN
function showNav(){
    if(settingsContainer.style.display==='none' || settingsContainer.style.display===''){
        settingsContainer.style.display='block'
    }
    else{
        settingsContainer.style.display='none'
    }
}