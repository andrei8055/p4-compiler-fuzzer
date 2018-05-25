<?php
namespace taming\distances;
interface Distance {

    public function __construct();
    public function calculate($s1, $s2);

}