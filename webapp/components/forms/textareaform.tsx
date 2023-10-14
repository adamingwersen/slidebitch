"use client";

import axios from "axios";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { useForm } from "react-hook-form";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Textarea } from "@/components/ui/textarea";
import { toast } from "@/components/ui/use-toast";
import { STORAGE_KEYS, useLocalStorage } from "@/hooks/useLocalStorage";
import { zodResolver } from "@hookform/resolvers/zod";

// const firms = [
//   {
//     id: "mckinsey",
//     label: "McKinsey",
//   },
//   {
//     id: "bcg",
//     label: "BCG",
//   },
//   {
//     id: "baine",
//     label: "Baine",
//   },
// ] as const;

const FormSchema = z.object({
  querystring: z.string().max(250),
  // firms: z.array(z.string()).refine((value) => value.some((item) => item), {
  //   message: "You have to select at least one item.",
  // }),
});

export function TextareaForm({}) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [queryResults, setQueryResults] = useLocalStorage<QueryPayload>(
    STORAGE_KEYS.QUERY_RESULT,
    {
      queryString: "",
      queryResults: [],
    }
  );

  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    // defaultValues: {
    //   firms: ["mckinsey"],
    // },
  });

  const onSubmit = async (data: z.infer<typeof FormSchema>) => {
    toast({
      title: "You submitted the following values:",
      description: (
        <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
          <code className="text-white">{JSON.stringify(data, null, 2)}</code>
        </pre>
      ),
    });
    try {
      setLoading(true);
      const resp = await axios.post(`http://localhost:8000/query`, data);
      const queryResp: QueryResult[] = resp.data;
      setQueryResults({
        queryString: data.querystring,
        queryResults: queryResp,
      });

      router.refresh();
      router.push("/queryResult");
    } catch (error: any) {
      console.log("fuck");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="w-2/4 space-y-6">
        <FormField
          control={form.control}
          name="querystring"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Query consulting database</FormLabel>
              <FormControl>
                <Textarea
                  placeholder="Insert anything you'd like to research here"
                  className="resize-none"
                  {...field}
                />
              </FormControl>
              <FormDescription>
                The more precise you are, the better results you'll get - but
                max 250 characters.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />

        <Button type="submit">Submit</Button>
      </form>
    </Form>
  );
}
