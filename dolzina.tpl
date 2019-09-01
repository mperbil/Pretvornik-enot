%import model
%rebase('base.tpl', title='Pretvarjanje_enot')



  <h1>PRETVARJANJE DOLŽINE</h1>

<br>
<form action="/pretvori/">
število: <input type="text" name="st">   
<br>
<text>Enota iz katere pretvarjamo</text>
<br>
<input type="radio" name="enota1" value="km"> km<br>
<input type="radio" name="enota1" value="m"> m<br>
<input type="radio" name="enota1" value="dm"> dm<br>
<input type="radio" name="enota1" value="cm"> cm<br>
<input type="radio" name="enota1" value="mm"> mm<br>
<br>
<br>
<text>Enota v katero pretvarjamo</text>
<br>
<input type="radio" name="enota2" value="km"> km<br>
<input type="radio" name="enota2" value="m"> m<br>
<input type="radio" name="enota2" value="dm"> dm<br>
<input type="radio" name="enota2" value="cm"> cm<br>
<input type="radio" name="enota2" value="mm"> mm<br>
<button type="submit">Pretvori</button>
  
</form>
</br>
