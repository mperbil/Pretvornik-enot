%import model
%rebase('base.tpl', title='Pretvarjanje_enot')



  <h1>PRETVARJANJE TEŽE</h1>

<br>
<form action="/pretvori/">
število: <input type="text" name="st">   
<br>
<text>Enota iz katere pretvarjamo</text>
<br>
<input type="radio" name="enota1" value="t"> tona<br>
<input type="radio" name="enota1" value="kg"> kg<br>
<input type="radio" name="enota1" value="g"> g<br>
<input type="radio" name="enota1" value="mg"> mg<br>
<br>
<br>
<text>Enota v katero pretvarjamo</text>
<br>
<input type="radio" name="enota2" value="t"> tona<br>
<input type="radio" name="enota2" value="kg"> kg<br>
<input type="radio" name="enota2" value="g"> g<br>
<input type="radio" name="enota2" value="mg"> mg<br>
<button type="submit">Pretvori</button>
  
</form>
</br>