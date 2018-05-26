<?php
namespace db;
class TestCaseEntity
{
    private $id;
    private $test;
    private $error;
    private $file;
    private $seed;
    private $known;
    private $is_medoid;
    private $cluster;


    /**
     * Accept an array of data matching properties of this class
     * and create the class
     *
     * @param array $data The data to use to create
     */
    public function __construct(array $data) {
        // no id if we're creating
        if(isset($data['id'])) {
            $this->id = $data['id'];
        }
        $this->test = $data['test'];
        $this->error = $data['error'];
        $this->file = $data['file'];
        $this->seed = $data['seed'];
        $this->known = $data['known'];
        if(isset($data['is_medoid'])) {
            $this->is_medoid = $data['is_medoid'];
        }
        if(isset($data['cluster'])) {
            $this->cluster = $data['cluster'];
        }

    }

    /**
     * @param mixed $error
     */
    public function setError($error)
    {
        $this->error = $error;
    }

    /**
     * @return mixed
     */
    public function getError()
    {
        return $this->error;
    }

    /**
     * @param mixed $file
     */
    public function setFile($file)
    {
        $this->file = $file;
    }

    /**
     * @return mixed
     */
    public function getFile()
    {
        return $this->file;
    }

    /**
     * @param mixed $id
     */
    public function setId($id)
    {
        $this->id = $id;
    }

    /**
     * @return mixed
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * @param mixed $seed
     */
    public function setSeed($seed)
    {
        $this->seed = $seed;
    }

    /**
     * @return mixed
     */
    public function getSeed()
    {
        return $this->seed;
    }

    /**
     * @param mixed $test
     */
    public function setTest($test)
    {
        $this->test = $test;
    }

    /**
     * @return mixed
     */
    public function getTest()
    {
        return $this->test;
    }

    /**
     * @param mixed $known
     */
    public function setKnown($known)
    {
        $this->known = $known;
    }

    /**
     * @return mixed
     */
    public function getKnown()
    {
        return $this->known;
    }

    /**
     * @param mixed $cluster
     */
    public function setCluster($cluster)
    {
        $this->cluster = $cluster;
    }

    /**
     * @return mixed
     */
    public function getCluster()
    {
        return $this->cluster;
    }

    /**
     * @param mixed $is_medoid
     */
    public function setIsMedoid($is_medoid)
    {
        $this->is_medoid = $is_medoid;
    }

    /**
     * @return mixed
     */
    public function getIsMedoid()
    {
        return $this->is_medoid;
    }



}