let info_1 = document.getElementById('info_1');




window.addEventListener('scroll', () =>{
    let val = window.ScrollY;
    
    info_1.style.left = val * 2 + 'px';
}