import { useMemo } from "react";
import katex from "katex";

export default function MathText({ text, className }) {
  const parts = useMemo(() => splitMath(text || ""), [text]);
  return (
    <span className={className}>
      {parts.map((p, i) =>
        p.math ? (
          <span
            key={i}
            className={p.block ? "math-block" : "math-inline"}
            dangerouslySetInnerHTML={{ __html: renderSafe(p.content, p.block) }}
          />
        ) : (
          <span key={i}>{p.content}</span>
        )
      )}
    </span>
  );
}

function renderSafe(content, block) {
  try {
    return katex.renderToString(content, { throwOnError: false, displayMode: block });
  } catch {
    return content;
  }
}

function splitMath(text) {
  const parts = [];
  let i = 0;
  while (i < text.length) {
    if (text.startsWith("$$", i)) {
      const end = text.indexOf("$$", i + 2);
      if (end === -1) {
        parts.push({ math: false, content: text.slice(i) });
        break;
      }
      parts.push({ math: true, block: true, content: text.slice(i + 2, end) });
      i = end + 2;
    } else if (text[i] === "$") {
      const end = text.indexOf("$", i + 1);
      if (end === -1) {
        parts.push({ math: false, content: text.slice(i) });
        break;
      }
      parts.push({ math: true, block: false, content: text.slice(i + 1, end) });
      i = end + 1;
    } else {
      const nextDollar = text.indexOf("$", i);
      const chunk = nextDollar === -1 ? text.slice(i) : text.slice(i, nextDollar);
      parts.push({ math: false, content: chunk });
      i += chunk.length;
    }
  }
  return parts;
}