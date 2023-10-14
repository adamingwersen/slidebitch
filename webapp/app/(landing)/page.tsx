import { useState } from "react";

import { TextareaForm } from "@/components/forms/textareaform";
import { STORAGE_KEYS, useLocalStorage } from "@/hooks/useLocalStorage";

const LandingPage = () => {
  return (
    <div className="flex flex-col justify-center items-center m-10">
      <TextareaForm></TextareaForm>
    </div>
  );
};
export default LandingPage;
