<?php
namespace taming;

class Taming {
    //comment
    /** @var  \db\TestCaseEntity[]  */
    private $cases;
    private $algorithm;

    public function __construct($cases, $algorithmName) {
        $this->cases = $cases;
        switch(strtolower($algorithmName)) {
            case 'levenshtein':
                $this->algorithm = new distances\Levenshtein();
                break;
            default:
                $this->algorithm = new distances\Levenshtein();
                break;
        }
    }

    public function tame(){
        $sortedCases = [];
        $rndCaseKey = array_rand($this->cases);
        $case = $this->cases[$rndCaseKey];
        $sortedCases[] = $case;
        unset($this->cases[$rndCaseKey]);

        while(count($this->cases) > 0) {
            $caseKey = $this->getNext($case);
            $case = $this->cases[$caseKey];
            $sortedCases[] = $case;
            unset($this->cases[$caseKey]);
        }

        return $sortedCases;
    }

    /**
     * @param $currentCase \db\TestCaseEntity
     * @return int
     */
    private function getNext($currentCase){
        $furthestCaseKey = 0;
        $furthestDistance = 0;


        foreach($this->cases as $caseKey => $case) {

            $distance = $this->algorithm->calculate($currentCase->getError(), $case->getError());

            if($distance > $furthestDistance) {
                $furthestDistance = $distance;
                $furthestCaseKey = $caseKey;
            }
        }


        return $furthestCaseKey;
    }
}