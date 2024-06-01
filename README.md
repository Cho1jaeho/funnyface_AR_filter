# funnyface_AR_filter
<h2>Introduction</h2>
<p>I tried to implement AR filters that are widely used on TikTok or Instagram using OpenCV in Python.</p>
<p>This program makes your face rediculous using AR technology.</p>
<ul>
  <li>example</li>
</ul>
<table>
  <tr>
    <th scope="col">instagram</td>
    <th scope="col">tiktok</td>
  </tr>
  <tr>
    <td><img src="https://github.com/Cho1jaeho/funnyface_AR_filter/assets/162866830/12d2c4e3-441d-4264-972b-530e5478b48a" width=200 height=300></td>
    <td><img src="https://github.com/Cho1jaeho/funnyface_AR_filter/assets/162866830/106e5e52-b227-4c8c-93be-4ccb47f12ea5"</td>
  </tr>
</table>
<h2>Technique used to create program</h2>
<p>To synthesize the filter into the face, the face location information must be recognized.</p>
<p>I used <code>dlib</code> to solve this problem.</p>
<ul>
  <li>Used for face recognition and landmark detection</li>
  <li>For more information, <a href="http://dlib.net/">dlib formal document</a></li>
</ul>
<h2>Contents</h2>
<ul>
  <li><code>sample/shape_predictor_68_face_landmarks.dat</code>: File containing face landmark information</li>
  <li><code>sample/rest</code>: original image files of filter</li>
  <li><code>overlay_transparent</code>: function to synthesize an image on your face</li>
  <li><code>main.py</code>: main function of program</li>
  <li>filters</li>
  <ul>
    <li><code>bulge_effect.py</code>: filter that applies bulge effect to your face</li>
    <li><code>concave_effect.py</code>: filter that applies concave effect to your face</li>
    <li><code>dog_filter.py</code>: filter that applies dog effect to your face</li>
    <li><code>enlarge_eyes_and_mouth.py</code>: filter that enlarges your eyes and mouth</li>
    <li><code>hamster_filter.py</code>: filter that makes hamster pictures come out with your face</li>
    <li><code>hat_filter.py</code>: filter that applies hat effect to your head</li>
    <li><code>sunglasses_filter.py</code>: filter that applies sunglasses effect to your eyes</li>
  </ul>
</ul>
<h2>How to use</h2>
<p>Download samples and files, and run <code>main.py</code>.</p>
<p>When you run it, your face will appear on the webcam without the filter applied.</p>
<p>Whenever you press tab key, filter changes.</p>
