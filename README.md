<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EranGoldman/urlShortener">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">urlShortener</h3>

  <p align="center">
    This is a quick test for urlShortener in python 3.8
    <br />
    <a href="https://github.com/EranGoldman/urlShortener"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EranGoldman/urlShortener">View Demo</a>
    ·
    <a href="https://github.com/EranGoldman/urlShortener/issues">Report Bug</a>
    ·
    <a href="https://github.com/EranGoldman/urlShortener/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a quick test for urlShortener in python 3.8
I'll use some docker and terraform for easy deployment to Digitalocean

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8 
* Docker 
* Docker compose.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EranGoldman/urlShortener.git
   ```
2. Run docker-compose
	```sh	
	docker-compose up -d
	```


<!-- USAGE EXAMPLES -->
## Usage

* Go to http://localhost:5000 for the main page.
* Use a shorten url http://localhost:5000/ABCDEF to forward the user to the target url
* use the API
  * Create new shorten url :
  ```sh
  curl -X POST http://localhost:5000/api/v1/shorten/<URL in url encoded format>
  ```
  * Get the unshortened url of a link
  ```sh
  curl -X POST http://localhost:5000/api/v1/lookup/<hash>
  ```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EranGoldman/urlShortener/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/erangoldman) - erangoldman@gmail.com

Project Link: [https://github.com/EranGoldman/urlShortener](https://github.com/EranGoldman/urlShortener)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

[First page template](https://colorlib.com/wp/template/colorlib-search-4/)  
[README template](https://github.com/OSKWalker/Best-README-Template)


