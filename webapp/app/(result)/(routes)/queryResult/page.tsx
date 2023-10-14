"use client";
import { RotateCcw } from "lucide-react";
import Link from "next/link";

import Result from "@/components/result";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Button } from "@/components/ui/button";
import { STORAGE_KEYS, useLocalStorage } from "@/hooks/useLocalStorage";

const QueryResultPage = () => {
  const [q, ,] = useLocalStorage(STORAGE_KEYS.QUERY_RESULT);
  const result = q as QueryPayload;
  return (
    <div className="flex flex-col justify-center items-center m-10">
      <div className="flex justify-center items-center m-10 w-full ">
        <div className="flex justify-center">
          <Alert className="flex flex-row justify-center items-center bg-grey-300 bg-clip-text">
            {" "}
            <AlertDescription className="">
              <b>Your query:</b> <span>{result.queryString}</span>
            </AlertDescription>
          </Alert>
          <div className="flex items-center">
            <Button variant="outline" className="mx-5">
              <RotateCcw className="mr-2 h-4 w-4" />
              <Link href="/">Retry</Link>
            </Button>
          </div>
        </div>
      </div>

      <Result queryResults={result.queryResults as QueryResult[]} />
    </div>
  );
};
export default QueryResultPage;
