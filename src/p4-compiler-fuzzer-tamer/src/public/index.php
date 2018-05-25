<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

require '../vendor/autoload.php';


$config['displayErrorDetails'] = true;
$config['addContentLengthHeader'] = false;

$config['db']['host']   = 'localhost';
$config['db']['user']   = 'p4-compiler-fuzzer';
$config['db']['pass']   = 'p4-compiler-fuzzer';
$config['db']['dbname'] = 'fuzzer';


$app = new \Slim\App(['settings' => $config]);
$container = $app->getContainer();

$container['logger'] = function($c) {
    $logger = new \Monolog\Logger('my_logger');
    $file_handler = new \Monolog\Handler\StreamHandler('../logs/app.log');
    $logger->pushHandler($file_handler);
    return $logger;
};

$container['db'] = function ($c) {
    $db = $c['settings']['db'];
    $pdo = new PDO('mysql:host=' . $db['host'] . ';dbname=' . $db['dbname'],
        $db['user'], $db['pass']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    return $pdo;
};

$container['view'] = function ($container) {
    $viewOptions = [];
//    $viewOptions = [
//        'cache' => '../cache'
//    ];
    $view = new \Slim\Views\Twig('../templates', $viewOptions);

    // Instantiate and add Slim specific extension
    $basePath = rtrim(str_ireplace('index.php', '', $container->get('request')->getUri()->getBasePath()), '/');
    $view->addExtension(new Slim\Views\TwigExtension($container->get('router'), $basePath));

    return $view;
};

$app->get('/cases', function ($request, $response, $args) {

    $this->logger->addInfo("Reading test cases");
    $mapper = new TestCaseMapper($this->db);
    $testCases = $mapper->getTestCases();

    $testCases = [1,2,3];

    return $this->view->render($response, 'test-cases.html', [
        'testCases' => $testCases
    ]);
})->setName('profile');


$app->run();

