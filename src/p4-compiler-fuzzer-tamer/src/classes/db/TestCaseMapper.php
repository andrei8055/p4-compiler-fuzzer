<?php
namespace db;
class TestCaseMapper extends Mapper
{
    public function getTestCases() {
        //For testing purpose since complexity is n^2; Maybe fix it to n logn
        $sql = "SELECT * FROM bugs WHERE id in(2794, 2795, 106, 107, 108, 109, 110, 140, 141, 154, 138) ";
        $stmt = $this->db->query($sql);
        $results = [];
        while($row = $stmt->fetch()) {
            $results[] = new TestCaseEntity($row);
        }
        return $results;
    }

}