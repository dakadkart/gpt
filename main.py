<?php

/*
Plugin Name: Open CS
Plugin URI: https://opencs.free.nf
Description: This is a plugin to generate text using the Hugging Face GPT-2 model.
Version: 1.0.0
Author: GPT
Author URI: https://opencs.free.nf
License: GPL v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: opencs
Domain Path: /languages
*/

header('Content-Type: text/plain');

// Set the API URL
$apiUrl = 'https://api-inference.huggingface.co/models/gpt2';

// Set the API token
$apiToken = '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';

// Get the user input
$userInput = $_POST['user-input'];

// If the user input is empty, display an error message
if (empty($userInput)) {
  echo 'Please enter some input before submitting.';
  exit;
}

// Create a curl object
$ch = curl_init();

// Set the POST request URL
curl_setopt($ch, CURLOPT_URL, $apiUrl);

// Set the POST request headers
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  'Content-Type: application/json',
  'Authorization: Bearer ' . $apiToken
));

// Set the POST request body
$requestBody = json_encode([
  'inputs' => $userInput
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, $requestBody);

// Execute the curl request
$response = curl_exec($ch);

// Check for errors
if ($response === false) {
  // Display an error message to the user
  echo 'Error: ' . curl_error($ch);
  exit;
}

// Close the curl object
curl_close($ch);

// Decode the JSON response
$responseData = json_decode($response);

// Check if the response is an error
if (isset($responseData->error)) {
  // Display the error message to the user
  echo 'Error: ' . $responseData->error;
  exit;
}

// Get the generated text
$generatedText = $responseData->generated_text;

// Convert the generated text to plain text
$generatedText = strip_tags($generatedText);

// If the generated text is defined, display it to the user
if (isset($generatedText)) {
  echo $generatedText;
}

?>
