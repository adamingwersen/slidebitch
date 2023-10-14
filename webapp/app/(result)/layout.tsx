const ResultLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <main className="h-full  overflow-auto">
      <div className="h-full w-full"> {children}</div>
    </main>
  );
};

export default ResultLayout;
