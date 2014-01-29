experiment_title = ''
required_data = {}
required_data['head'] = '''
<head>
  <title>BS3:Computer Graphics Lab</title>
  <link rel="stylesheet" type="text/css" href="../../normalize.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Bootstrap -->
  <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" media="screen">    
  <link rel="stylesheet" type="text/css" href="../style.css">
  <link rel="stylesheet" type="text/css" href="../bstyle.css">
  <link href='http://fonts.googleapis.com/css?family=Actor' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro' rel='stylesheet' type='text/css'>
  <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../../assets/js/html5shiv.js"></script>
      <script src="../../assets/js/respond.min.js"></script>
      <![endif]-->
      <style type="text/css">
        body{
          background-color: #f4f4f4;
        }
      </style>  
</head> '''

required_data['navbar'] = '''
<nav class="navbar navbar-default visible-lg" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <a class="navbar-brand" href="#">'''+experiment_title+'''</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse navbar-ex1-collapse desk-nav">
          <ul class="nav navbar-nav">
            <li style="border-right: 1.5px solid white;"><a href="index.html">Lab Manual</a></li>
            <li style="border-right: 1.5px solid white;"><a href="simulation.html">Simulation</a></li>
            <li><a href="quiz.html">Quiz</a></li>
          </ul>
          <a href="../index.html"><span class="glyphicon glyphicon-home pull-right"></span></a>
        </div><!-- /.navbar-collapse -->
      </nav>

      <div class="hidden-lg">
      <nav class="navbar navbar-default mobile-nav" role="navigation">
      <div class="nav navbar-nav pull-right">
    <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span></a>&nbsp;<a href="simulation.html"><span class="glyphicon glyphicon-play-circle"></span></a>&nbsp;<a href="quiz.html"><span class="glyphicon glyphicon-tower"></span>&nbsp;&nbsp;</a><a href="../index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;</a>
  </div>
    </nav>
    <p class="experiment-mobile-title">'''+experiment_title+'''</p>
    </div>'''

required_data['lab-index'] = '''
<div class="col-lg-2 visible-lg lab-index">
    <ul class="nav nav-pills nav-stacked">
      <li class="active"><a href="#intro">Introduction</a></li>
      <li><a href="#theory">Theory</a></li>
      <li><a href="#obj">Objective</a></li>
      <li><a href="#proc">Procedure</a></li>
      <li><a href="#further-reading">Further Reading</a></li>
    </ul>
  </div>
'''

required_data['scripts'] = '''
<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="http://code.jquery.com/jquery.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
'''     