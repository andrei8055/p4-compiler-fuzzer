<?php
class TestCaseEntity
{
    private $id;
    private $test;
    private $error;
    private $file;
    private $seed;
    private $known;


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

}