function create(i,p)  {
    $ (document).ready(function(){
        i.click(function() {
            i.toggle();
            p.toggle();
        });
        p.click(function(){
            i.toggle();
            p.toggle();
        });
    });
   
}
create($('.brand'), $('.drop'));
create($('.brand2'), $('.drop2'));
create($('.brand3'), $('.drop3'));

$(".range").hover(function () {
    $(this).children(".red").slideToggle(1000, "linear");
});