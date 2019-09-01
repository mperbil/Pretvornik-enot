%import model
%rebase('base.tpl', title='Pretvarjanje_enot')



  <h1>PRETVARJANJE PROSTORNINE</h1>
<br>
<form action="/pretvori/">
število: <input type="text" name="st">   
<br>
<text>Enota iz katere pretvarjamo</text>
<br>
<input type="radio" name="enota1" value="hl"> hl<br>
<input type="radio" name="enota1" value="l"> l<br>
<input type="radio" name="enota1" value="dl"> dl<br>
<input type="radio" name="enota1" value="cl"> cl<br>
<input type="radio" name="enota1" value="ml"> ml<br>
<br>
<br>
<text>Enota v katero pretvarjamo</text>
<br>
<input type="radio" name="enota2" value="hl"> hl<br>
<input type="radio" name="enota2" value="l"> l<br>
<input type="radio" name="enota2" value="dl"> dl<br>
<input type="radio" name="enota2" value="cl"> cl<br>
<input type="radio" name="enota2" value="ml"> ml<br>
<button type="submit">Pretvori</button>

  
</form>
</br>