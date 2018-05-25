<?php
class TestCaseMapper extends Mapper
{
    public function getTestCases() {
        $sql = "SELECT * FROM bugs";
        $stmt = $this->db->query($sql);
        $results = [];
        while($row = $stmt->fetch()) {
            $results[] = new TestCaseEntity($row);
        }
        return $results;
    }

}