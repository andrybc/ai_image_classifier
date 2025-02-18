import React, { useState } from "react";
import { Card, CardContent } from "./components/ui/card";
import { Button } from "./components/ui/button";
import { FileInput } from "./components/ui/file_input";
import { Select, SelectItem } from "./components/ui/select";

const categories = ["Animals", "Objects", "Scenery", "Faces", "Vehicles"];
const API_URL = "https://classifier.andrybc.dev/api";


export default function ImageClassifierPage() {
    const [selectedCategory, setSelectedCategory] = useState("Animals");
    const [uploadedFile, setUploadedFile] = useState(null);
    const [classificationResult, setClassificationResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event) => {
        if (event.target.files && event.target.files[0]) {
            setUploadedFile(event.target.files[0]);
            setClassificationResult(null); // Clear previous result
        }
    };

    const classifyImage = async () => {
        if (!uploadedFile) {
            alert("Please upload an image first.");
            return;
        }

        const formData = new FormData();
        formData.append("image", uploadedFile); // Use "image" instead of "file"
        formData.append("category", selectedCategory);

        setIsLoading(true);
        try {
            const response = await fetch(`${API_URL}/classify`, {
                method: "POST",
                body: formData,
            });

            const data = await response.json();

            if (response.ok) {
                setClassificationResult(
                    `Class: ${data.result.split(",")[0]}, Confidence: ${data.result.split(": ")[2]}`
                );
            } else {
                setClassificationResult(`Error: ${data.error}`);
            }
        } catch (error) {
            setClassificationResult("Error connecting to API.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center p-8">
            <Card className="w-full max-w-lg shadow-2xl rounded-2xl p-6">
                <CardContent className="space-y-6">
                    <h1 className="text-2xl font-bold text-gray-800 text-center">
                        AI Image Classifier
                    </h1>
                    <p className="text-center text-gray-600">
                        Upload an image and select the category to classify.
                    </p>

                    <div className="space-y-4">
                        <FileInput
                            id="file-input"
                            onChange={handleFileChange}
                            className="w-full border p-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                        <Select
                            value={selectedCategory}
                            onChange={(e) => setSelectedCategory(e.target.value)}
                            className="w-full border p-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        >
                            {categories.map((category) => (
                                <SelectItem key={category} value={category}>
                                    {category}
                                </SelectItem>
                            ))}
                        </Select>
                    </div>

                    {uploadedFile && (
                        <div className="mt-4">
                            <img
                                src={URL.createObjectURL(uploadedFile)}
                                alt="Uploaded preview"
                                className="w-full h-auto rounded-lg border"
                            />
                        </div>
                    )}

                    <Button
                        onClick={classifyImage}
                        className="w-full bg-blue-600 text-white font-semibold py-2 rounded-lg hover:bg-blue-700 transition"
                        disabled={isLoading}
                    >
                        {isLoading ? "Classifying..." : "Classify Image"}
                    </Button>

                    {classificationResult && (
                        <div className="mt-4 p-4 bg-green-100 border border-green-300 rounded-lg text-green-800">
                            <p className="text-center font-medium">{classificationResult}</p>
                        </div>
                    )}
                </CardContent>
            </Card>
        </div>
    );
}
