function funcall(){ 
document.getElementById("pagecompleted").style.display='none'; 
document.getElementById("pagepending").style.display='none';
document.getElementById("pageall").style.display='block'; 
}

function funccompleted(){ 
document.getElementById("pagecompleted").style.display='block'; 
document.getElementById("pagepending").style.display='none';
document.getElementById("pageall").style.display='none'; 
}

function funcpending(){ 
document.getElementById("pagecompleted").style.display='none'; 
document.getElementById("pagepending").style.display='block';
document.getElementById("pageall").style.display='none'; 
}