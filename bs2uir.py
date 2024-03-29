import re
from bs4 import BeautifulSoup
myhtml = '''
<!DOCTYPE html>
<html>
<head></head>
<body>

<div id="experiment"> <!-- The Experiment Document Container-->

	<!-- The lab Header contains the logo and the name of the lab, usually 
		 displayed on the top of the page -->

	<header id="experiment-header" class="default">

		<div id="experiment-header-logo" class="logo">
			<!-- Enclose the logo image of your lab or write it in text -->
			<img src="../images/logo.jpg" />
		</div>

		<div id="experiment-header-heading" class="heading">
			<!-- Write the name of your lab and link it to the home page of 
				 your lab (h1 tag is preferred while writing your lab name)
			-->
			<a href="../index.php">Computer Graphics</a>	
		</div>

		<!-- Add any additional element you want to add to the lab header,
			 For example : Help (Enclosing them with suitable div is 
			 recommended) -->

	</header>


	<!-- The lab article is the main content area where all the experiment
		 content sits -->
	<article id="experiment-article">

		<!-- The lab article has an header, optional navigational menu, 
			 number of sections, an optional sidebar and a closing footer 
		-->
		<div id="experiment-article-breadcrumb" class="breadcrumb">
		</div>
    
		<header id="experiment-article-heading" class="heading">
			<!-- You can add a welcome message or title of the experiment
				 here -->
			Points &amp; Co-ordinate Systems
			<!-- Add any additional element if required with proper 
				 enclosing -->
		</header>

		<!-- Navigation menu is useful to organize the view of multiple
			 sections inside the article -->
		<nav id="experiment-article-navigation" class="default">
			<ul id="experiment-article-navigation-menu">
				<!-- The menu can be dynamically generated to contain the
					 headings of your sections or instead write the menu 
					 items of your choice individually enclosedu in <li> 
					 tag as shown below -->
			</ul>
		</nav>

		<!-- All the sections of your lab or experiment can be enclosed 
			 together with a div element as shown below -->
		<div id="experiment-article-sections">

			<!-- First section of the article -->
			<section id="experiment-article-section-1">

				<div id="experiment-article-section-1-icon" class="icon">
					<img src="../images/introduction.jpg" />
				</div>	

				<!-- The heading for the section can be enclosed in a div 
					 tag. -->
				<div id="experiment-article-section-1-heading" 
					 class="heading">
					Introduction
				</div>

				<!-- Write the section content inside a paragraph element, 
					 You can also include images with <img> tag -->
				<div id="experiment-article-section-1-content" 
					 class="content">	
					<p>
						This experiment explains how points and co-ordinate systems are used together to represent two and three dimensional shapes.
					</p>
					<img src="media/vector.svg.png" alt="Position Vector" 
						 style="width:220px; height:185px;">
				</div>

			</section>


			<!-- Second section of the article-->
			<section id="experiment-article-section-2">

				<div id="experiment-article-section-2-icon" class="icon">
					<!-- Enclose the icon image of your lab. -->
					<img src="../images/theory.jpg" />
				</div>

				<!-- The heading for the section can be enclosed in a div 
					 tag. -->
				<div id="experiment-article-section-2-heading" 
					 class="heading">
					Theory
				</div>

				<!-- Write the section content inside a paragraph element, 
					 we can also include images with <img> tag -->
				<div id="experiment-article-section-2-content" 
					 class="content">
					<img src="media/Cartesian-coordinate-system.svg" 
						 alt="2-d vectors" 
						 style="float:left; width:200px; height: 200px; margin-right:10px; background-color: #fff;" />
					<p>
						Two dimensional points are represented as perpendicular distance from orthogonal axes, usually called X and Y. So (2,3) represents a point 2 units from the y-axis and 3 units from the x-axis. If the co-ordinate axes are non-orthogonal, the point represents distances taken parallel to the axes.
					</p>
					<p>
						Three dimensional points are represented as distances from each of the three planes formed by the axes. So (2,3,4) represents a point 2 units from YZ-plane, 3 units from XZ-plane and 4 units from XY-plane.
					</p>
					<p>
						Coordinates can be 'homogenized' by adding an extra value to the tuple. In 3 dimensions, points are represented as (x,y,z,w) which is equivalent to (x/w, y/w, z/w) in ordinary co-ordinates. This is a convenient representation used heavily in computer graphics as it allows writing the common operations such as translation as a linear product.
					</p>
				</div>
			</section>


			<section id="experiment-article-section-3">
        
				<div id="experiment-article-section-3-icon" class="icon">
					<img src="../images/objective.jpg" />
				</div>

				<div id="experiment-article-section-3-heading" 
					 class="heading">
					Objective
				</div>

				<div id="experiment-article-section-3-content" 
					 class="content">
					<p>
						Objective of this experiment is to understand the representation of points in 2D or 3D space with orthogonal as well as non-orthogonal coordinate systems.
					</p>
				</div>

			</section>


			<section id="experiment-article-section-4">

				<div id="experiment-article-section-4-icon" class="icon">
					<img src="../images/simulation.jpg" />
				</div>

				<div id="experiment-article-section-4-heading" 
					 class="heading">
					Experiment
				</div>

				<div id="experiment-article-section-4-content" 
					 class="content">
					<p>
						<ol type=1 start=1>
						<li>
							Please download the appropriate Virtual Lab Graphics package below. <br/>
							<b><a href="../VirtualLabGraphics.zip">Download</a></b> <br/>
						</li>
						<li>
							Save the <b>VirtualLabGraphics.zip</b> file and double click it to extract.
						</li>
						<li>
							Run the Start.jar in the extracted folder (VirtualLabGraphics folder) to start the experiments.
							<ul>
							<li>
								Windows/MacOSX users can start the experiment by double clicking the Start.jar file.
							</li>
							<li>
								Linux users should run Start.jar by executing the following command in the terminal. <br/>
								Change to the Virtual Lab Directory. <br/>
								<i><b>$</b> cd VirtualLabGraphics/</i> <br/>
								Execute the experiment using the command: <br/>
								<i><b>$</b> java -jar Start.jar</i>
							</li>
							</ul>
						</li>
						<li>
						<b>Alternate Method:</b> If you are not able to start the experiment by the above procedures, you can try the alternate method given below.
							<ul>
							<li>
								Alternatively, Linux/MacOSX users can start the experiment by as described below. <br/>
								Change to the Virtual Lab Directory. <br/>
								<i><b>$</b> cd VirtualLabGraphics/</i> <br/>
								Execute the experiment using the command: <br/>
								<i><b>$</b> ./Experiment.sh 1</i>
							</li>
							<li>
								Alternatively, Windows users can start the experiment by double clicking the Experiment1.bat file.
							</li>
							</ul>
						</li>
						</ol>
						<!-- Place or link to your experiment java applet or 
							 flash file here. -->
					</p>
				</div>

			</section>

			<section id="experiment-article-section-5">
   
				<div id="experiment-article-section-5-icon" class="icon">
					<img src="../images/manual.jpg" />
				</div>

				<div id="experiment-article-section-5-heading" 
					 class="heading">
					Manual
				</div>

				<div id="experiment-article-section-5-content" 
					 class="content">
					<script type="text/javascript" src="../js/pageload.js"> </script>
					<div id="page">
						<a href="../vlabs-manual.pdf">Download Manual</a>
						<script type="text/javascript">
							loadPage('index.html');
						</script>
					</div>
				</div>

			</section>


			<section id="experiment-article-section-6">

				<div id="experiment-article-section-6-icon" class="icon">
					<img src="../images/quizzes.jpg" />
				</div>

				<div id="experiment-article-section-6-heading" 
					 class="heading">
					Quizzes
				</div>

				<div id="experiment-article-section-6-content" 
					 class="content">

				<script type="text/javascript" src="evaluate.js"></script>
				<form name="quiz" method="post">
					<img src="media/quiz.png" 
						 alt="Quiz Points" 
						 style="width:400px; height: 377px; background-color: #fff;" />

					<p>
					<b>Q1.</b> 
					Enter the points with brackets and a comman between. Ex. (5, -3)<br> 
					<ol start='a'>
					<li>
						Point A
						<input type="text" name="q1_a" value="" size=10 />
					</li>
					<li>
						Point B
						<input type="text" name="q1_b" value="" size=10 />
					</li>
					<li>
						Point C
						<input type="text" name="q1_c" value="" size=10 />
					</li>
					<li>
						Point D
						<input type="text" name="q1_d" value="" size=10 />
					</li>
					<li>
						Point E
						<input type="text" name="q1_e" value="" size=10 />
					</li>
					</ol>
					</p>
					<p>
					<b>Q2.</b>
					What is the point whose distance from XY plane is 3, YZ plane is -4 and XZ plane is 9 ? <br/>
					<input type="radio" name="q2" id="q2" value="1"> &nbsp;&nbsp;
					(3, 0, -4) <br/>
					<input type="radio" name="q2" id="q2" value="2"> &nbsp;&nbsp;
					(-4, 3, 9) <br/>
					<input type="radio" name="q2" id="q2" value="3"> &nbsp;&nbsp;
					(-4, 9, 3) <br/>
					<input type="radio" name="q2" id="q2" value="4"> &nbsp;&nbsp;
					(-4, 9, 9)
					</p>
					<p>
					<b>Q3.</b>
					Convert the coordinate (12, 24, 42, 6) from homogeneous form to ordinary cartesian coordinates. <br/>
					<input type="radio" name="q3" id="q3" value="1"> &nbsp;&nbsp;
					(4, 2, 7) <br/>
					<input type="radio" name="q3" id="q3" value="2"> &nbsp;&nbsp;
					(7, 2, 4) <br/>
					<input type="radio" name="q3" id="q3" value="3"> &nbsp;&nbsp;
					(2, 4, 7) <br/>
					<input type="radio" name="q3" id="q3" value="4"> &nbsp;&nbsp;
					(2, 4, 4)
					</p>
					<p>
					<input type="button" value="Evaluate" class="button" onclick="eval();" />
					</p>
				</form>
				</div>

			</section>


			<section id="experiment-article-section-7">

				<div id="experiment-article-section-7-icon" class="icon">
					<img src="../images/procedure.jpg" />
				</div>

				<div id="experiment-article-section-7-heading" 
					 class="heading">
					Procedure
				</div>

				<div id="experiment-article-section-7-content" 
					 class="content">
					<p>
						This experiment is designed to teach how points and co-ordinate systems are represented in computer graphics. The tree at the right shows a point and the associated co-ordinate system.
					</p>
					<p>
						Start by editing the co-ordinates of the point and comparing how the point gets displayed. The co-ordinates can be edited by clicking on the node under <i><b>Instance->Shape->Vertices</b></i>
					</p>
					<p>
						Now try modifying the co-ordinate system's origin and axis directions. This can be done by clicking on the nodes under <i><b>Instance->Co-ordinate System</b></i>. Notice how the point is redrawn using the modified co-ordinate system. Also notice how the absolute co-ordinates are displayed.
					</p>
					<p>
						All points shown within '[' and ']' use homogeneous co-ordinates, i.e., the fourth component <i><b>w</b></i> acts as a scaling factor for calculating the cartesian co-ordinates. Modify this component and notice how the point's co-ordinates get scaled.
					</p>
					<p>
						You can also modify the absolute co-ordinates of the point and see how the relative co-ordinates get calculated with respect to the co-ordinate system.
					</p>
					<p>
						This scene is currently shown in 2D but you can switch to 3D under the Display tab and perform all the previous actions in 3D. Drag with the right mouse button to rotate the view and use the mouse wheel to zoom in and out.
					</p>
				</div>
					
			</section>
			
		
			<section id="experiment-article-section-8">
   
				<div id="experiment-article-section-8-icon" class="icon">
					<img src="../images/readings.jpg" />
				</div>

				<div id="experiment-article-section-8-heading" 
					 class="heading">
					Further Readings
				</div>

				<div id="experiment-article-section-8-content" 
					 class="content">
					<ul>	
					<li>
					<a href="http://en.wikipedia.org/wiki/Cartesian_coordinate_system">
						Wikipedia: Cartesian Coordinate System
					</a>
					</li>
					<li>
					<a href="http://en.wikipedia.org/wiki/Homogeneous_coordinates#Use_in_computer_graphics">
						Wikipedia: Homogeneous Coordinates
					</a>
					</li>
					</ul>
				</div>

			</section>

			<section id="lab-article-section-6">
				<div id="lab-article-section-6-heading" class="heading">
					Feedback
				</div>

				<div id="lab-article-section-6-content" class="content">
					<p>
					<ul>
						<li><a href="http://virtual-labs.ac.in/feedback/?lab=cse18?lab=cse18">Feedback</a></li>
					</ul>
					</p>
				</div>
			</section>

		</div>


		<!-- An article can have a sidebar that contain related links and 
			 additional material (however it is kept optional at this 
			 moment) -->
		<aside id="lab-article-sidebar" class="default">
			<!-- put the content that you want to appear in the sidebar -->	
		</aside>


		<!-- Article footer can display related content and additional links 
		-->						
		<footer id="lab-article-footer" class="default">
			<!-- Put the content that you want to appear here -->
		</footer>

	</article>


	<!-- Links to other labs, about us page can be kept the lab footer -->
	<footer id="lab-footer" class="default footer">
		<!-- Put the content here-->
	</footer>

</div>		

</body>
</html>
'''

soup = BeautifulSoup(myhtml)
one = soup.find_all('section',id=re.compile("experiment-article-section-[0-9]"))
#print str(one.find_all('div',class_="heading")[0].text)
# contentsli = one.find_all('div',class_="content")[0].contents
# content = ''
# for i in contentsli:
# 	if i != '\n':
# 		content = content+str(i)
# print content

for oneart in one:
	heading = str(oneart.find_all('div',class_="heading")[0].text).strip()
	contents_list = oneart.find_all('div',class_="content")[0].contents
	content = ''
	for i in contents_list:
		if i != '\n':
			content = content+str(i)
	print '<html><body><h1>'+heading+'</h1><hr>'+content+'</body></html>'
#print soup.section
#mylist = soup.section.find_all(id=re.compile("experiment-article-section-[0-9]"))

