%import model
%rebase('base.tpl', title='Pretvarjanje_enot')


<center>
  <h1>REZULTAT</h1>
{{st}}<text> </text>{{vhodna}}<text> je</text>
<h2>
{{result}}
</h2>

</center>
<form action="/nazaj/">
    <button type="submit">NAZAJ</button>
  </form>