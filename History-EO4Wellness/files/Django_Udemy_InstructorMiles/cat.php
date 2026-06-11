<?php

class Cat {

 public $color = 'black';

  function meow() {
      print($this->color);
  }

}

$tom_the_cat = new Cat();

print($tom_the_cat->color);

$spot_the_cat = new Cat();

