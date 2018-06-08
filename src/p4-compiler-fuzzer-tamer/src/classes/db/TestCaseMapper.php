<?php
namespace db;
class TestCaseMapper extends Mapper
{
    public function getTestCases() {
        //For testing purpose since complexity is n^2; Maybe fix it to n logn
        $sql = "SELECT * FROM bugs WHERE id < 3200";
        $stmt = $this->db->query($sql);
        $results = [];
        while($row = $stmt->fetch()) {
            $results[] = new TestCaseEntity($row);
        }
        return $results;
    }

    public function getClusteredTestCases() {
        $sql = "SELECT b.*, tb.is_medoid, tb.cluster FROM bugs b INNER JOIN tamed_bugs tb on b.id = tb.bug_id ORDER BY cluster";
        $stmt = $this->db->query($sql);
        $results = [];
        while($row = $stmt->fetch()) {
            $results[] = new TestCaseEntity($row);
        }
        return $results;
    }

}