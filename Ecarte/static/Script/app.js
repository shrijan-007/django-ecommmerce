
var tablet_width = "(max-width : 768px)";
var mobile_width = "(max-width : 475px)";
var laptop_width = "(max-width : 1024px)";
var cartHtml ="<a href='/cart' style ='display:block;text-decoration:none;margin-right:8px;' class = 'linkwrapper-span'><i class='fas fa-shopping-cart' style ='font-size:20px;color:black;'></i></a></li>" ;

var navbar = document.getElementById('block-navigation');
var Linkwrapper = document.getElementById('navbar-link');
var navlinksList = document.getElementById('nav-link-list');
var nav_logo = document.getElementById('navlogo');
let headerElement = document.getElementById('media-division');
let headerElementnavhtml = headerElement.innerHTML;
let initialHtml =  Linkwrapper.innerHTML;
function responsive(screen_width){
    if(screen_width.matches){
        navlinksList.style.display = "none";
        Linkwrapper.innerHTML = cartHtml+"<span style ='display:block;' id = 'Link-menu' class = 'linkwrapper-span' onclick='showmenu()'><i class='fas fa-bars' style ='font-size:20px;'></i></span>";
    }
    else{
        navlinksList.style.display = "flex";
        Linkwrapper.innerHTML = initialHtml;
        headerElement.innerHTML = "";
    }
}


console.log(headerElementnavhtml);
function showmenu(){
        headerElement.innerHTML = initialHtml;
        Linkwrapper.innerHTML = "<span style ='display:block;' id = 'Link-menu-close' class = 'linkwrapper-span' onclick='closemenu()'><i class='fas fa-times' style ='font-size:20px;'></i></span>";
        }
function closemenu(){
    headerElement.innerHTML = "";
    Linkwrapper.innerHTML = cartHtml+"<span style ='display:block;' id = 'Link-menu' class = 'linkwrapper-span' onclick='showmenu()'><i class='fas fa-bars' style ='font-size:20px;'></i></span>";
}
screen_width = window.matchMedia(tablet_width);
responsive(screen_width);
screen_width.addListener(responsive);
// Carousel code
var carouselItems = document.getElementsByClassName("img-container");
var caruselLength = carouselItems.length;
var sliderFrame = document.getElementById('slider-frame');
var slideLeft  = document.getElementById('scroll-left');
var slideRight = document.getElementById('scroll-right');
let currentSlide = 1;
sliderFrame.style.transition = "all 0.3s linear";
slideLeft.addEventListener('click',()=> {
    if(currentSlide > 1){
        var slideBy =  0;
        if (currentSlide == 2) {
            slideBy = 0;
        } else if(currentSlide == 3) {
            slideBy = 33;
        }

        sliderFrame.style.transform = "translateX(-" + slideBy +"%)";
        currentSlide = currentSlide - 1;
        
    }
});
slideRight.addEventListener('click',()=> {
    if(currentSlide < caruselLength){
        var slideBy = (currentSlide *33.3);
        sliderFrame.style.transform = "translateX(-" + slideBy +"%)";
        currentSlide = currentSlide + 1;
    
    }
});
var carouselContent = document.getElementsByClassName("ca-maincontentContainer");


sliderFrame.addEventListener('transitionend',()=>{

    for(let i = 0; i<caruselLength;i++){
        carouselContent[i].classList.remove('animatedText');
    }
    carouselContent[currentSlide-1].classList.add('animatedText'); 
});

function togglefilterbar(){
    var btnflt = document.getElementById("filterbar");
    if (btnflt.style.display === 'none') {
        btnflt.style.display = 'flex';
        btnflt.style.width = (document.getElementById('filtersection').clientWidth - 16) + 'px';
    } else {
        btnflt.style.display = 'none';
    }

}


