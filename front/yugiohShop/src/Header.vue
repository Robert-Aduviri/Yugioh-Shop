<template>

  <div id="vue-header">
  
    <nav class="arribabarfamiliar"></nav>
    <nav class="arribabar">
       <ul>
          <li style="width:10%;"><a class="textologo">GCS</a></li>    
          <li style="width:15%;"><img src="./assets/grandpa.jpg"  style="width:100px;height:60px;"></img></li>
          <li style="width:50%;"><input type="text" style="height:20px;color:black;font-size:120%;"></li>
          <li style="width:10%;"><a><i class="material-icons" style="color:black;">search</i></a></li>
          <li><a class="signinletters">Sign In</a></li>
          <li><a><i class="material-icons" style="color:black;">shopping_cart</i></a></li>
       </ul>
    </nav>
    <nav class="arribabarfamiliar"></nav>
   <nav >
    <div class="nav-wrapper" style="background-color:black;color:white; font-weight:bold;height:50px ">
     
      <a href="#" data-activates="mobile-demo" class="button-collapse" ><i class="material-icons">menu</i></a>
      <ul class="left hide-on-med-and-down">
           <li ><a href="#" class="cardslinks">Monster's Cards</a></li>
          <li ><a href="#" class="cardslinks">Magic Cards</a></li>
          <li ><a href="#" class="cardslinks">Trap Cards</a></li>
          <li ><a href="#" class="cardslinks">Structure Decks</a></li>
          <li ><a href="#" class="cardslinks">Materials</a></li>
          <li ><a href="#" class="cardslinks">Grandpa's Paneton</a></li>
          <li ><a href="#" >About the Grandpa's Store</a></li>
          
      </ul>
      <ul class="side-nav" id="mobile-demo">
          <li ><a href="#" class="cardslinks">Monster's Cards</a></li>
          <li ><a href="#" class="cardslinks">Magic Cards</a></li>
          <li ><a href="#" class="cardslinks">Trap Cards</a></li>
          <li ><a href="#" class="cardslinks">Structure Decks</a></li>
          <li ><a href="#" class="cardslinks">Materials</a></li>
          <li ><a href="#" class="cardslinks">Grandpa's Paneton</a></li>
          <li ><a href="#" >About the Grandpa's Store</a></li>
      </ul>
    </div>
  </nav>
          
  </div>

</template>

<script>
export default { }
</script>

<style lang="scss">
.textologo{
    color:black;
    text-align:center;
    font-size:250%;
    font-family: Impact, Charcoal, sans-serif;
}
.arribabar{
    background-color:rgb(234, 239, 245);
    height:60px;
}
.arribabarfamiliar{
    background-color:rgb(234, 239, 245);
    height:30px;
}
.signinletters{
  color:black;
  font-size:120%;
  font-weight:bold;
}
.cardslinks{
border-right-style: solid;
border-width: 5px;
margin:auto;
}

</style>
