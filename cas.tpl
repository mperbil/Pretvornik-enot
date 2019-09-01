%import model
%rebase('base.tpl', title='Pretvarjanje_enot')



  <h1>PRETVARJANJE ČASA</h1>

<br>
<form action="/pretvori/">
število: <input type="text" name="st">   
<br>
<text>Enota iz katere pretvarjamo</text>
<br>
<input type="radio" name="enota1" value="d"> dan<br>
<input type="radio" name="enota1" value="h"> ura<br>
<input type="radio" name="enota1" value="min"> minuta<br>
<input type="radio" name="enota1" value="s"> sekunda<br>
<br>
<br>
<text>Enota v katero pretvarjamo</text>
<br>
<input type="radio" name="enota2" value="d"> dan<br>
<input type="radio" name="enota2" value="h"> ura<br>
<input type="radio" name="enota2" value="min"> minuta<br>
<input type="radio" name="enota2" value="s"> sekunda<br>
<button type="submit">Pretvori</button>
  
</form>
</br>