"use client";

import { ExternalLink } from "lucide-react";
import Link from "next/link";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "./ui/badge";
import { Button } from "./ui/button";

interface ResultProps {
  queryResults: QueryResult[];
}

export const Result: React.FC<ResultProps> = ({ queryResults }) => {
  return (
    <div className="flex flex-col justify-center">
      {queryResults.map((queryResult, index) => (
        <Card key={index} className="mb-5">
          <CardHeader className="pt-2">
            <CardTitle className="text-lg">
              {queryResult.metadata.title}
            </CardTitle>

            <CardDescription>
              {queryResult.metadata.description}
            </CardDescription>
          </CardHeader>
          <CardFooter className="flex justify-end items-end">
            {" "}
            <Badge
              className={`mx-5 mt-3  color: ${
                queryResult.distance < 1 ? "bg-green-400" : "bg-orange-400"
              }`}
            >
              {"Similarity score = " + queryResult.distance.toFixed(3)}
            </Badge>
            <Button>
              <ExternalLink className="mr-2 h-4 w-4" />
              <Link href={queryResult.metadata.link}>Go to report</Link>
            </Button>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
};

export default Result;
