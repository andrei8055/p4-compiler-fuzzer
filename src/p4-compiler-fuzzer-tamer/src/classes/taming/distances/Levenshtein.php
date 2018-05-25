<?php
namespace taming\distances;

class Levenshtein implements Distance {

    public function __construct() {

    }

    public function calculate($s1, $s2)
    {
        $l1 = strlen($s1);
        $l2 = strlen($s2);
        $dis = range(0,$l2);

        for($x=1;$x<=$l1;$x++){
            $dis_new[0]=$x;
            for($y=1;$y<=$l2;$y++){
                $c = ($s1[$x-1] == $s2[$y-1])?0:1;
                $dis_new[$y] = min($dis[$y]+1,$dis_new[$y-1]+1,$dis[$y-1]+$c);
            }
            $dis = $dis_new;
        }

        return $dis[$l2];
    }

}