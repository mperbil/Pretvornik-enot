%import model

%rebase('base.tpl', title='Enote')


<center>
  <marquee><h1 style="color:#0000cc">PRETVARJANJE ENOT</h1></marquee>

  <text>
  Katero mersko količino želite pretvarjati?
<br>Pretvarjamo lahko dolžino, prostornino, težo in čas.
  </text>
  <hr color="red">

<br>
  <form action="/na_dolzino/">
    <button type="submit">DOLŽINO</button>
  </form>
<br>
  <form action="/na_prostornino/">
    <button type="submit">PROSTORNINO</button>
  </form>
<br>
  <form action="/na_tezo/">
    <button type="submit">TEŽO</button>
  </form>
<br>  
  <form action="/na_cas/">
    <button type="submit">ČAS</button>
  </form>
<br> 
</center>







